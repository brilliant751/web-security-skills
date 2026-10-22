---
name: 35-api-auth-abuse
description: 测试 API 认证与令牌滥用时使用。Use when 用户提到 API key 滥用、bearer token、头部信任、限流绕过、签名重放时加载。
metadata:
  title: API认证滥用
  category: vuln
---

# API认证滥用

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
