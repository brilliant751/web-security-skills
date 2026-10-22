---
name: 23-jwt-token-attacks
description: 测试 JWT 与令牌攻击时使用。Use when 流量中出现 JWT/Bearer token，或用户提到 JWT 算法混淆、none 算法、密钥混淆、JWKS 滥用、声明篡改时加载。
metadata:
  title: JWT与令牌攻击
  category: vuln
---

# JWT与令牌攻击

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
