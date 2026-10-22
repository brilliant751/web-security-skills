# AGENTS.md

本仓库是面向 AI Agent 的 Web 安全测试技能库，共 40 个技能。所有技能入口位于 `skills/NN-slug/SKILL.md`，详细手册位于同目录的 `references/` 下。

## 目录约定

```text
skills/
└── NN-slug/
    ├── SKILL.md          # 唯一入口
    └── references/
        ├── 主手册.md      # 必备
        └── ...           # 场景集 / 专题手册
```

- `NN` 为 01–40 的两位编号，`slug` 为小写英文短名，目录名必须与 `SKILL.md` 的 `name` 完全一致。
- 技能根目录只允许 `SKILL.md`，不得放置其他 Markdown。
- 所有参考文档必须放在 `references/`，命名用中文短名（如 `主手册.md`、`场景集.md`、`sqlmap进阶.md`）。
- 中文展示名放 `metadata.title`，分类放 `metadata.category`（`recon` / `vuln` / `bypass` / `workflow`）。

## SKILL.md 格式

```markdown
---
name: 05-sql-injection
description: 测试 SQL 注入时使用。Use when 目标存在数据库交互（登录框、搜索、列表、分页、排序），或用户提到 SQLi、sqlmap、union 注入、盲注、报错注入、WAF 绕过矩阵、多数据库利用时加载。
metadata:
  title: SQL注入
  category: vuln
---

# SQL注入

## 何时使用
- ...

## 文件路由
| 文件 | 用途 |
|---|---|
| [主手册.md](references/主手册.md) | 主手册 |

## 上手顺序
1. ...
2. ...
```

- `description` 必须包含触发条件（`Use when ...`），长度不超过 1024 字符。
- 入口正文保持精简（不超过 100 行），只写路由与上手顺序，细节放进 `references/`。
- 路由表必须覆盖 `references/` 下的全部文档。

## 链接层级

| 位置 | 写法 |
|---|---|
| 入口 → 参考文档 | `references/xxx.md` |
| `references/` 内互链 | `xxx.md` |
| 跨技能 | `../../NN-slug/references/xxx.md` |

## 新增或修改技能

1. 新建 `skills/NN-slug/` 与 `references/`。
2. 按上述模板编写 `SKILL.md`。
3. 运行校验：

   ```bash
   python scripts/validate_skills.py
   ```

4. 同步更新 `README.md` 的技能索引。

## 校验项

`scripts/validate_skills.py` 会检查：目录名与 `name` 一致、命名规则、`description` 长度、入口行数、根目录无散落文档、`references/` 中存在主手册、路由表覆盖全部参考文档、站内链接可达。提交前必须通过。

## 内容规范

- 漏洞技能正文保留上游英文原文；文件命名与 frontmatter 使用中文。
- 修改上游正文时只做必要的路径与命名调整，不随意改写技术内容。
- 不提交真实目标、凭据、个人隐私或未脱敏的测试数据。
