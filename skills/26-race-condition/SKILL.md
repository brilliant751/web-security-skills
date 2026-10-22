---
name: 26-race-condition
description: 测试竞态条件时使用。Use when 用户提到竞态、并发、TOCTOU、HTTP/2 单包攻击、Turbo Intruder、重复领券/提现时加载。
metadata:
  title: 竞态条件
  category: vuln
---

# 竞态条件

## 何时使用

- 上述 description 中列出的场景命中任意一条时，先读本入口，再按需下钻

## 文件路由

| 文件 | 用途 |
|---|---|
| [主手册.md](references/主手册.md) | 主手册（正文保留原文） |

## 上手顺序

1. 读主手册开头的 ROUTING / 概述章节，确认命中本技能
2. 按主手册章节执行测试（正文为英文实战手册，章节标题可检索）
3. 命中具体场景（如某厂商 WAF、某引擎）时再读对应附属手册
