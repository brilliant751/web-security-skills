---
name: 07-command-injection
description: 测试命令注入时使用。Use when 目标存在系统命令拼接特征（ping、文件名处理、后台执行功能），或用户提到 CMDi、命令执行 RCE、通配符绕过、PHP disable_functions 绕过时加载。
metadata:
  title: 命令注入
  category: vuln
---

# 命令注入

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
