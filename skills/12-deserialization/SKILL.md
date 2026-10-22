---
name: 12-deserialization
description: 测试反序列化漏洞时使用。Use when 用户提到 Java/PHP/Python/.NET 反序列化、gadget 链、YAML/Pickle/BinaryFormatter/ViewState、中间件反序列化 RCE 时加载。
metadata:
  title: 反序列化
  category: vuln
---

# 反序列化

## 何时使用

- 上述 description 中列出的场景命中任意一条时，先读本入口，再按需下钻

## 文件路由

| 文件 | 用途 |
|---|---|
| [主手册.md](references/主手册.md) | 主手册（正文保留原文） |
| [Java利用链.md](references/Java利用链.md) | 附属手册 |

## 上手顺序

1. 读主手册开头的 ROUTING / 概述章节，确认命中本技能
2. 按主手册章节执行测试（正文为英文实战手册，章节标题可检索）
3. 命中具体场景（如某厂商 WAF、某引擎）时再读对应附属手册
