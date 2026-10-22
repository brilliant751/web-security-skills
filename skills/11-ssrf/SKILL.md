---
name: 11-ssrf
description: 测试 SSRF 时使用。Use when 目标存在 URL 拉取功能（预览、导入、webhook、头像抓取），或用户提到 SSRF、内网探测、云元数据、gopher 协议、URL 解析差异时加载。
metadata:
  title: SSRF服务端请求伪造
  category: vuln
---

# SSRF服务端请求伪造

## 何时使用

- 上述 description 中列出的场景命中任意一条时，先读本入口，再按需下钻

## 文件路由

| 文件 | 用途 |
|---|---|
| [主手册.md](references/主手册.md) | 主手册（正文保留原文） |
| [场景集.md](references/场景集.md) | 附属手册 |
| [URL解析技巧.md](references/URL解析技巧.md) | 附属手册 |

## 上手顺序

1. 读主手册开头的 ROUTING / 概述章节，确认命中本技能
2. 按主手册章节执行测试（正文为英文实战手册，章节标题可检索）
3. 命中具体场景（如某厂商 WAF、某引擎）时再读对应附属手册
