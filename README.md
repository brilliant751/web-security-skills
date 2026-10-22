# Web 漏洞技能集

整理自 [yaklang/hack-skills](https://github.com/yaklang/hack-skills)（MIT License）与 [Hi-FullHouse/CyberSecurity-Skills](https://github.com/Hi-FullHouse/CyberSecurity-Skills)（MIT License），共 **40 个技能**。归档顺序：**01–04 信息收集**（针对单站：端口 → 指纹 → 目录 → JS/API），**05–35 经典漏洞类型**，**36–38 绕过类**，**39 框架与组件已知漏洞（N-day）**，**40 漏洞报告生成**（把已确认的漏洞整理成补天／漏洞盒子可提交的报告）。

三类环节的区别：**05–35 按「输入点」测**（看到一个参数，判断它进到哪儿，配对应手法），**39 按「组件版本」测**（先认框架与版本，再对该版本的已知 CVE 逐项检索验证），**40 不测漏洞、只做交付**（输入是已人工复现的事实，输出是平台能收的报告，缺截图留标注交人工补）。39/40 放在末尾编号，是为了不打乱 05–35 已被提示词引用的既有编号。

## 目录结构

```text
.
├── AGENTS.md                     # 仓库约定（Agent 入口）
├── CLAUDE.md                     # 指向 AGENTS.md
├── README.md                     # 本索引
├── scripts/
│   └── validate_skills.py        # 结构、命名与链接校验
└── skills/
    └── NN-slug/                  # 一个技能一个目录，编号 01–40
        ├── SKILL.md              # 唯一入口：frontmatter + 文件路由表
        └── references/           # 全部参考文档（主手册 / 场景集 / 专题手册）
```

约定：

- 目录名 = `SKILL.md` 中 `name` 字段，格式 `NN-小写英文短名`，通过官方 Agent Skills 命名规则。
- 中文名称放在 `metadata.title`，分类放在 `metadata.category`（`recon` / `vuln` / `bypass` / `workflow`）。
- `description` 必须写清触发条件（`Use when ...`），长度不超过 1024 字符。
- 技能根目录只允许 `SKILL.md`；其余文档一律放入 `references/`，由入口的路由表按需加载。
- 链接层级：入口写 `references/xxx.md`；`references/` 内互链直接写 `xxx.md`；跨技能写 `../../NN-slug/references/xxx.md`。

## 技能索引

### 信息收集（01–04，针对单个网站）

| 编号 | 目录 | 技能 |
|---|---|---|
| 01 | [`skills/01-port-service-scan/`](skills/01-port-service-scan/) | Nmap、Masscan、RustScan 端口扫描与服务指纹 |
| 02 | [`skills/02-tech-fingerprint/`](skills/02-tech-fingerprint/) | Web 指纹（WhatWeb/Wappalyzer）、中间件版本、WAF 识别（wafw00f） |
| 03 | [`skills/03-dir-brute/`](skills/03-dir-brute/) | dirsearch/gobuster：后台路径、备份文件、.git/.svn、编辑器入口（附源码管理泄露原文） |
| 04 | [`skills/04-js-api-recon/`](skills/04-js-api-recon/) | JS 文件分析（接口路径、硬编码密钥、sourcemap）、Swagger 文档、隐藏端点、注释泄露（附 API 信息收集原文） |

### 经典漏洞类型（05–35）

| 编号 | 目录 | 技能 |
|---|---|---|
| 05 | [`skills/05-sql-injection/`](skills/05-sql-injection/) | SQL 注入（附场景集、SQLMap 高级用法） |
| 06 | [`skills/06-xss/`](skills/06-xss/) | XSS 跨站脚本（附进阶技巧、场景集） |
| 07 | [`skills/07-command-injection/`](skills/07-command-injection/) | 命令注入 |
| 08 | [`skills/08-file-upload/`](skills/08-file-upload/) | 不安全文件上传（附场景集） |
| 09 | [`skills/09-path-traversal-lfi/`](skills/09-path-traversal-lfi/) | 路径穿越与文件包含 |
| 10 | [`skills/10-xxe/`](skills/10-xxe/) | XML 外部实体注入（附场景集） |
| 11 | [`skills/11-ssrf/`](skills/11-ssrf/) | SSRF 服务端请求伪造（附场景集、URL 解析技巧） |
| 12 | [`skills/12-deserialization/`](skills/12-deserialization/) | 反序列化（附 Java Gadget 链） |
| 13 | [`skills/13-ssti/`](skills/13-ssti/) | 模板注入（附引擎 payload 集、场景集） |
| 14 | [`skills/14-nosql-injection/`](skills/14-nosql-injection/) | NoSQL 注入 |
| 15 | [`skills/15-el-injection/`](skills/15-el-injection/) | 表达式注入 |
| 16 | [`skills/16-jndi-injection/`](skills/16-jndi-injection/) | JNDI 注入 |
| 17 | [`skills/17-crlf-injection/`](skills/17-crlf-injection/) | CRLF 注入 |
| 18 | [`skills/18-xslt-injection/`](skills/18-xslt-injection/) | XSLT 注入 |
| 19 | [`skills/19-csv-formula-injection/`](skills/19-csv-formula-injection/) | CSV 公式注入 |
| 20 | [`skills/20-email-header-injection/`](skills/20-email-header-injection/) | 邮件头注入 |
| 21 | [`skills/21-idor/`](skills/21-idor/) | 越权访问 |
| 22 | [`skills/22-auth-bypass/`](skills/22-auth-bypass/) | 认证绕过 |
| 23 | [`skills/23-jwt-token-attacks/`](skills/23-jwt-token-attacks/) | JWT 与令牌攻击 |
| 24 | [`skills/24-oauth-oidc/`](skills/24-oauth-oidc/) | OAuth 配置错误 |
| 25 | [`skills/25-business-logic/`](skills/25-business-logic/) | 业务逻辑漏洞（附方法论、检查清单、场景集） |
| 26 | [`skills/26-race-condition/`](skills/26-race-condition/) | 竞态条件 |
| 27 | [`skills/27-cors-misconfig/`](skills/27-cors-misconfig/) | CORS 配置错误（附场景集） |
| 28 | [`skills/28-csrf/`](skills/28-csrf/) | 跨站请求伪造 |
| 29 | [`skills/29-clickjacking/`](skills/29-clickjacking/) | 点击劫持 |
| 30 | [`skills/30-open-redirect/`](skills/30-open-redirect/) | 开放重定向 |
| 31 | [`skills/31-subdomain-takeover/`](skills/31-subdomain-takeover/) | 子域名接管 |
| 32 | [`skills/32-dns-rebinding/`](skills/32-dns-rebinding/) | DNS 重绑定 |
| 33 | [`skills/33-api-recon/`](skills/33-api-recon/) | API 信息收集 |
| 34 | [`skills/34-api-bola/`](skills/34-api-bola/) | API 授权与 BOLA |
| 35 | [`skills/35-api-auth-abuse/`](skills/35-api-auth-abuse/) | API 认证滥用 |

### 绕过类（36–38）

| 编号 | 目录 | 技能 |
|---|---|---|
| 36 | [`skills/36-access-bypass/`](skills/36-access-bypass/) | 401/403 访问绕过 |
| 37 | [`skills/37-waf-bypass/`](skills/37-waf-bypass/) | WAF 绕过（附产品矩阵） |
| 38 | [`skills/38-csp-bypass/`](skills/38-csp-bypass/) | CSP 绕过 |

### 框架与组件已知漏洞（39）

| 编号 | 目录 | 技能 |
|---|---|---|
| 39 | [`skills/39-nday-vuln/`](skills/39-nday-vuln/) | N-day 四步链路：版本识别 → 联网检索 CVE/PoC → 逐项验证 → 判定归档（含框架 payload 形态对照表、ThinkPHP 5.0.x 实测样本、curl 转义规则） |

### 报告与提交（40）

| 编号 | 目录 | 技能 |
|---|---|---|
| 40 | [`skills/40-vuln-report-generate/`](skills/40-vuln-report-generate/) | 漏洞报告九段结构（标题/影响资产/类型/等级/描述/复现步骤/请求与响应/危害说明/修复建议）、逐段写法与退单点、**各类漏洞的验证上限表**（验到哪一步就停，含两家平台的越界红线）、证据留法（截图缺口标注约定）、危害等级判定（含敏感字段判定尺子）、补天与漏洞盒子字段差异、**会直接判定重复或忽略的规则**（同源合并 / 禁止拆分 / 弱口令 / 越界）、AI 辅助报告红线（两家公告）、提交后进度与返工、提交前自检清单 |

## 使用方式

1. Agent 先读 `AGENTS.md` 了解仓库约定。
2. 按任务命中 `description` 后，读取对应 `skills/NN-slug/SKILL.md` 的路由表。
3. 只加载当前需要的 `references/` 文档，避免一次性吞掉全部手册。

## 校验

```bash
python scripts/validate_skills.py
```

检查项：目录名与 `name` 一致、命名规则、`description` 长度、入口行数、根目录无散落文档、`references/` 中存在主手册、路由表覆盖全部参考文档、站内链接可达。CI 在 `.github/workflows/validate.yml` 中执行同一脚本。

## 来源与许可

- 漏洞技能正文保留英文原文，文件命名与 frontmatter 为中文；信息收集 01/02 来自 CyberSecurity-Skills（中文原文），03/04、39、40 为自建中文技能（03/04 蒸馏自 hack-skills，附属原文保留英文）。
- 已按需移除原型污染、类型松散比较、SAML、GraphQL、GhostBits、请求走私、Host 头攻击、HTTP/2 攻击、Web 缓存欺骗、HTTP 参数污染、悬挂标记注入等技能。
- 上游项目均为 MIT License，本仓库同样以 MIT License 发布，见 [LICENSE](LICENSE)。
