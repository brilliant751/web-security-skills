---
name: 08-file-upload
description: 测试文件上传漏洞时使用。Use when 目标存在上传点（头像、附件、导入），或用户提到上传绕过、MIME/扩展名绕过、图片马、IIS/Apache/Nginx 解析漏洞、编辑器路径时加载。
metadata:
  title: 不安全文件上传
  category: vuln
---

# 不安全文件上传

## 何时使用

- 上述 description 中列出的场景命中任意一条时，先读本入口，再按需下钻

## 文件路由

| 文件 | 用途 |
|---|---|
| [主手册.md](references/主手册.md) | 主手册（正文保留原文） |
| [场景集.md](references/场景集.md) | 附属手册 |

## 上手顺序

1. 读主手册开头的 ROUTING / 概述章节，确认命中本技能
2. 按主手册章节执行测试（正文为英文实战手册，章节标题可检索）
3. 命中具体场景（如某厂商 WAF、某引擎）时再读对应附属手册
