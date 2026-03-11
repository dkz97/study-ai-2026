# study-ai-2026

> 从零开始学 Python × AI 工程实践记录
> Learning Python & AI Engineering from Scratch

---

## 关于本项目 / About

本项目记录了我从 Java 转型 Python，并系统学习 AI 工程实践的完整过程（7周计划）。
内容包括 Python 基础语法、API 调用、LLM 集成，以及两个完整的 AI 小项目。

This repo documents my journey from Java to Python, with a focus on AI engineering practice (7-week plan).
It includes Python fundamentals, API usage, LLM integration, and two complete AI mini-projects.

---

## 项目结构 / Structure

```
study-ai-2026/
├── week01-03_python-basics/          # Python 学习记录 / Python learning notes
│   ├── 01_syntax/                    # 基础语法 / Basic syntax
│   ├── 02_http_api/                  # HTTP & API 调用 / HTTP & API calls
│   └── 03_llm_integration/           # LLM 集成 / LLM integration
│
├── week04-06_crypto-research-copilot/ # 项目一 / Project 1
│   ├── v1_news_summary/              # 每日币圈新闻汇总 / Daily crypto news summary
│   └── v2_rag_qa/                    # RAG 问答研究助手 / RAG-based Q&A assistant
│
└── week07_ai-workflow-tool/           # 项目二 / Project 2
    └── ...                           # AI 资料搜索整理工具 / AI research workflow tool
```

---

## 学习计划 / Weekly Plan

| 周次 / Week | 主题 / Topic | 目标 / Goal |
|-------------|--------------|-------------|
| Week 1–2 | Python 基础语法 | 变量、控制流、函数、OOP |
| Week 3 | HTTP / API / LLM 集成 | requests、OpenAI API、LangChain |
| Week 4 | Crypto Copilot v1 | 每日币圈新闻汇总 |
| Week 5 | Crypto Copilot v2 (RAG) | 升级为可问答研究助手 |
| Week 6 | 上线 & 投递 | 部署项目，开始投递简历 |
| Week 7 | AI Workflow Tool | Crypto/金融资料延伸搜索整理 |

---

## 技术栈 / Tech Stack

- **语言 / Language**: Python 3.11+
- **AI / LLM**: OpenAI API, LangChain
- **向量数据库 / Vector DB**: ChromaDB
- **HTTP**: requests, httpx
- **其他 / Others**: python-dotenv, pydantic

---

## 项目一：Crypto Research Copilot

> 目标：从每日新闻汇总工具升级为可问答的研究助手

- v1：抓取币圈新闻 → LLM 生成摘要 → 每日推送
- v2：新闻入向量库 → RAG 检索 → 自然语言问答

📁 [week04-06_crypto-research-copilot/](./week04-06_crypto-research-copilot/)

---

## 项目二：AI Workflow Tool

> 目标：针对 Crypto / 金融资料，进行延伸搜索和结构化整理

📁 [week07_ai-workflow-tool/](./week07_ai-workflow-tool/)

---

## 运行环境 / Setup

```bash
# 1. 克隆项目 / Clone the repo
git clone https://github.com/dkz97/study-ai-2026.git
cd study-ai-2026

# 2. 创建虚拟环境 / Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. 安装依赖（按项目目录） / Install dependencies (per project)
pip install -r week04-06_crypto-research-copilot/requirements.txt

# 4. 配置环境变量 / Configure environment variables
cp week04-06_crypto-research-copilot/.env.example week04-06_crypto-research-copilot/.env
# 编辑 .env，填入真实的 API Key / Edit .env with your real API keys
```
