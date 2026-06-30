# Harness Engineering 研究笔记

> 记录日期：2026-03-27
> 背景：读到一篇关于 Anthropic/OpenAI/Stripe 等公司 Harness Engineering 实践的文章，与 spec-first skill 进行对比分析

---

## 核心发现

### 同一模型，换个 Harness 效果翻倍

| 来源 | 数据 |
|------|------|
| Nate B Jones | 同一模型，Harness 不同，成功率 42% → 78% |
| LangChain | 同一模型 (gpt-5.2-codex)，只改 Harness，Terminal Bench 排名从三十名开外进前五 |
| Anthropic | Solo 模式 20min/$9 出来的东西功能是坏的；Harness 模式 6h/$200 出来能玩的游戏 |
| Pi Research | 一个下午内，仅通过修改 Harness，提升了 15 个不同 LLM 的编程能力 |

**结论：在当前节点，优化模型外面的壳，回报率可能比等下一代模型更高。**

---

## 三代进化

| 阶段 | 时间 | 核心关注 |
|------|------|---------|
| Prompt Engineering | 2022-2024 | 怎么写好一条指令 |
| Context Engineering | 2025 | 动态构建上下文（文件、对话、工具、知识库） |
| **Harness Engineering** | 2026.2- | 搭建让 Agent 持续、稳定、高质量工作的整套运行环境 |

比喻：
- Prompt Engineering = 写好一封邮件
- Context Engineering = 带上所有相关附件
- **Harness Engineering = 搭建整个工作环境**

---

## Harness Engineering 定义

来源：Mitchell Hashimoto（HashiCorp 联合创始人、Terraform 缔造者）

> 每当你发现 Agent 犯了一个错误，你就花时间去工程化一个解决方案，让它再也不会犯同样的错。

Anthropic 的补充：
> 模型不会评价自己的工作。让 Generator 自己评估刚写完的东西，它会自信地表示写得很好，即使质量明显不行。

解法：借鉴 GAN 思路，把**生成和评估拆成两个独立的 Agent**：
- Generator 负责写代码
- Evaluator 负责真机验收（用 Playwright 真机操作验证）
- 关键：让 Evaluator 变严格，比让 Generator 学会自我批评容易得多

---

## 头部公司实践

### OpenAI Codex
- 5 个月、100 万行代码、1500 个 PR，人类一行没写
- 核心规则：
  - 仓库是 Agent 唯一的知识来源
  - 架构约束不靠 prompt，靠 **linter**
  - 自主性得一步步给
  - **如果 PR 需要大改才能合并，问题不在 Agent，在 Harness**
- 新角色：**不写代码了。写规则。**

### Stripe
- 每周合并 1300+ PR，全部无人值守
- 架构：Blueprint 编排 = 确定性节点 + Agentic 节点
- 硬规则：**CI 最多跑两轮**，还失败直接转交人类
- 发现：**更多工具不等于更好表现**

### Anthropic
- 3 Agent 架构：Planner（展开需求） + Generator（逐 sprint 实现） + Evaluator（真机验收）
- 发现：evaluator 开箱即用是个差的 QA Agent，需要多轮校准

### Cursor
- Self-Driving Codebases：每小时约 1000 个 commit，一周超过 1000 万次工具调用
- **反直觉发现**：约束解空间，反而让 Agent 更有生产力

---

## spec-first vs 市场同类 skill 完整对比

### 对比对象
1. **Agent Harness** (clawhub.ai/bowen31337/harness) — OpenAI Codex 模式
2. **Spec Developer** (clawhub.ai/soponcd/spec-developer) — 规格文档驱动执行
3. **Constraint Engine** (clawhub.ai/leegitw/constraint-engine) — 失败驱动约束

### 横向对比表

| 维度 | spec-first | Agent Harness | Spec Developer | Constraint Engine |
|------|-----------|--------------|--------------|-----------------|
| 本质定位 | 人类审批驱动的开发流程 | 规则自动生成 + CI 强制 | 规格文档驱动的自动执行 | 失败驱动的安全护栏 |
| 触发条件 | 用户要求写代码 | repo 初始化/升级 | /spec-draft 等命令 | 观测到失败（阈值触发） |
| 目标澄清 | Q&A 对话确认 ✅ | 无（默认任务已清晰）❌ | 模板填充 | 隐含于失败日志 |
| 设计/Spec 形态 | 分块提案 + 逐块审批 | AGENTS.md + 架构文档 | Feature Spec 文档 | 约束规则列表 |
| 人类 Gate | 每阶段审批（强） | CI/Lint 结果（弱） | Draft 审批（一次） | 规则生成/Override（显式） |
| 执行模式 | 等 "go" 才执行 | 完全自主（最高） | 审批后自动循环 | Runtime 强制 |
| Evaluator | 无独立 Evaluator | CI + Lint | 自动化测试 | Circuit Breaker |
| 反馈循环 | 人类 checkpoint 报告 | CI 失败自动修复 | 测试失败阻塞 | Circuit breaker 状态 |
| 约束机制 | 对话中的边界约束 | Linter + 架构规则 | 无显式约束 | Runtime Circuit Breaker |
| 失败归因 | 人类决定 | PR 大改 = Harness 问题 | 代码问题 | 约束缺失/阈值突破 |

---

## spec-first 的优势（这些不需要改）

1. **主动前置澄清（Clarify Stage）**：唯一有 Q&A 主动挖掘目标的 skill
2. **强 Human-in-the-loop**：每阶段都有审批 Gate，人类全程在回路
3. **显式 "go" 才执行**：Execution 前有明确的心理边界
4. **范围蔓延时回到 Stage 1**：隐式失败归因逻辑（问题在系统设计，不在执行）

---

## 可借鉴的改进方向

### 1. 独立的 Evaluator 机制（高优先级）
**来源：** Anthropic 的 Generator-Evaluator 分离

**现状：** checkpoint 全靠人类判断完成度
**改进：** 在"go"之后、交付之前，加一道独立的 Evaluator 评审
- 不需要自动化测试（你没有测试基础设施）
- 可以是"真机验证清单"：手动验证几个关键路径
- 核心思路：**验收逻辑和生成逻辑分离**

### 2. Linter 化约束（中优先级）
**来源：** Agent Harness 的架构约束靠 linter

**现状：** SKILL.md 里的约束是自然语言，容易被忽略
**改进：** 把"技术红线"变成实际的 lint 规则文件
- 例：禁止直接删除文件、禁止未审批修改核心模块
- linter 强制 > 自然语言 prompt

### 3. 任务清单持续跟踪（中优先级）
**来源：** Spec Developer 的 Task 生命周期管理

**现状：** Implementation Plan 是一个静态清单，没有跟踪机制
**改进：** 
- Execution 阶段每完成一步，报告"我验证了什么"
- 形成一个可追溯的任务状态表

### 4. 失败日志 → 显式约束规则（低优先级，长期）
**来源：** Constraint Engine 的"失败驱动约束生成"

**现状：** AI 反复犯同一个错，靠记忆或临时提醒
**改进：** 当同一个错误出现 2 次以上，显式沉淀为一条规则
- 类似"这个配置已经跑不通了，不要再试"
- 可以记录在一个 `CONSTRAINTS.md` 文件里

### 5. AGENTS.md TOC 化（低优先级）
**来源：** Agent Harness 的 L1/L2/L3 分层索引

**现状：** SOUL.md / AGENTS.md 是线性文本
**改进：** 引入分层索引结构，让不同抽象级别的规则各归其位

---

## 相关资源

- [Anthropic Harness Engineering Blog](https://openai.com/index/harness-engineering/)
- [Mitchell Hashimoto: Engineer the Harness](https://mitchellh.com)
- [Pi Research: Improving 15 LLMs in One Afternoon](https://pi-research.com)
- [Terminal Bench 2.0 Leaderboard](https://terminal.bench)

---

*记录：Claw 🐾 | 2026-03-27*
