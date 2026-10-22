#!/usr/bin/env python3
"""校验仓库内所有 Skill 的命名、结构与链接。"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
NAME_RE = re.compile(r"^[0-9]{2}-[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\]\(([^)]+)\)")
FENCE_RE = re.compile(r"```.*?```", re.S)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
SKILL_REQUIRED = ("name", "description", "metadata")

errors = []


def rel(p: Path) -> str:
    return str(p.relative_to(ROOT)).replace("\\", "/")


def parse_frontmatter(text: str):
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not m:
        return None
    fields = {}
    current = None
    for line in m.group(1).splitlines():
        if not line.strip():
            continue
        if line.startswith((" ", "\t")) and current:
            fields[current] += "\n" + line.strip()
        elif ":" in line:
            current, value = line.split(":", 1)
            fields[current.strip()] = value.strip()
    return fields


def strip_code(text: str) -> str:
    """移除围栏代码块与行内代码，避免把示例里的括号误判为链接。"""
    text = FENCE_RE.sub("", text)
    return INLINE_CODE_RE.sub("", text)


def check_links(md: Path, text: str):
    for target in LINK_RE.findall(strip_code(text)):
        target = target.split("#", 1)[0].strip()
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        if target.startswith("file:///"):
            errors.append(f"{rel(md)}: 禁止使用 file:/// 链接 -> {target}")
            continue
        resolved = (md.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"{rel(md)}: 链接失效 -> {target}")


def main():
    if not SKILLS_DIR.is_dir():
        print("skills/ 目录不存在")
        return 1

    dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    if len(dirs) != 40:
        errors.append(f"技能数量应为 40，实际 {len(dirs)}")

    for skill in dirs:
        sk = skill / "SKILL.md"
        if not sk.exists():
            errors.append(f"{rel(skill)}: 缺少 SKILL.md")
            continue

        text = sk.read_text(encoding="utf-8-sig")
        fm = parse_frontmatter(text)
        if fm is None:
            errors.append(f"{rel(sk)}: frontmatter 缺失或格式错误")
            continue

        name = fm.get("name", "")
        if name != skill.name:
            errors.append(f"{rel(sk)}: name '{name}' 与目录名 '{skill.name}' 不一致")
        if not NAME_RE.match(name):
            errors.append(f"{rel(sk)}: name 不符合 NN-slug 格式 -> {name}")
        desc = fm.get("description", "")
        if not (1 <= len(desc) <= 1024):
            errors.append(f"{rel(sk)}: description 长度 {len(desc)}，应在 1-1024 之间")
        if "metadata" not in fm or not fm.get("metadata"):
            errors.append(f"{rel(sk)}: 缺少 metadata.title / metadata.category")
        else:
            meta = fm["metadata"]
            if "title:" not in meta:
                errors.append(f"{rel(sk)}: metadata 缺少 title")
            if "category:" not in meta:
                errors.append(f"{rel(sk)}: metadata 缺少 category")
        if len(text.splitlines()) > 100:
            errors.append(f"{rel(sk)}: 入口文件超过 100 行，应把细节移入 references/")

        for p in skill.iterdir():
            if p.is_file() and p.name != "SKILL.md":
                errors.append(f"{rel(p)}: 技能根目录只允许 SKILL.md，其余文档应放入 references/")

        refs = skill / "references"
        if not refs.is_dir():
            errors.append(f"{rel(skill)}: 缺少 references/ 目录")
            continue
        ref_files = sorted(refs.glob("*.md"))
        if not ref_files:
            errors.append(f"{rel(skill)}: references/ 为空")
        if not (refs / "主手册.md").exists():
            errors.append(f"{rel(skill)}: 缺少 references/主手册.md")

        linked = set()
        for target in LINK_RE.findall(text):
            target = target.split("#", 1)[0].strip()
            if target.startswith("references/"):
                linked.add((skill / target).resolve())
        for rf in ref_files:
            if rf.resolve() not in linked:
                errors.append(f"{rel(rf)}: 未被 SKILL.md 路由表引用")

        check_links(sk, text)
        for rf in ref_files:
            check_links(rf, rf.read_text(encoding="utf-8-sig"))

    if errors:
        print(f"校验失败，共 {len(errors)} 项：")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"校验通过：{len(dirs)} 个技能，结构、命名与链接均正常。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
