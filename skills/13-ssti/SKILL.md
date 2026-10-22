---
name: 13-ssti
description: 测试模板注入时使用。Use when 用户提到 SSTI、Jinja2/Twig/Smarty/Freemarker/Razor、{{7*7}} 探测、Flask PIN 计算、盲注 SSTI 时加载。
metadata:
  title: 模板注入
  category: vuln
---

# 模板注入

## 何时使用

- 上述 description 中列出的场景命中任意一条时，先读本入口，再按需下钻

## 文件路由

| 文件 | 用途 |
|---|---|
| [主手册.md](references/主手册.md) | 主手册（正文保留原文） |
| [引擎Payload.md](references/引擎Payload.md) | 附属手册 |
| [场景集.md](references/场景集.md) | 附属手册 |

## 上手顺序

1. 读主手册开头的 ROUTING / 概述章节，确认命中本技能
2. 按主手册章节执行测试（正文为英文实战手册，章节标题可检索）
3. 命中具体场景（如某厂商 WAF、某引擎）时再读对应附属手册
