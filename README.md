# 📊 Data Copilot — Autonomous GenAI Data Analyst Agent

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-PydanticAI-emerald.svg)](https://ai.pydantic.dev/)
[![LLM Engine](https://img.shields.io/badge/LLM-Groq%20API-orange.svg)](https://groq.com/)
[![Sandbox](https://img.shields.io/badge/Container-Docker-2496ED.svg)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Data Copilot** is an enterprise-grade, agentic AI data analyst that bridges natural language and database analytics. It translates free-form user questions into executable Python and SQL scripts, executes them securely within a sandboxed Docker container, and dynamically streams visual insight charts in real-time.

---

## 🌟 Key Features

- **🤖 Autonomous Agent Loop**: Built with **PydanticAI**, utilizing structured type validation, stateful conversation management, and native tool-calling.
- **🔒 Isolated Execution Sandbox**: Executes generated Python/SQL code safely within a locked-down **Docker container** to protect host systems.
- **⚡ High-Speed LLM Inference**: Leverages **Groq API** (LLaMA 3+) for near-instantaneous code generation and analytical reasoning.
- **📊 Dynamic Visualizations**: Intercepts generated `*.png` chart artifacts from Matplotlib/Seaborn and streams them directly into the UI.
- **🗄️ Relational Database Analytics**: Seamlessly interfaces with **PostgreSQL** to inspect schemas, execute complex queries, and aggregate data.
- **🔄 Self-Correction & Error Recovery**: Automatically catches runtime execution errors and feeds them back to the LLM for iterative code correction.

---

## 🏗️ System Architecture

Data Copilot decouples the user-facing interface, agent reasoning engine, and execution sandbox to maintain maximum security, scalability, and performance.

```mermaid
flowchart TD
    %% User Layer
    subgraph USER [" 💻 USER LAYER "]
        UI["Streamlit Chat Interface"]
    end

    %% Agent Engine
    subgraph AGENT [" 🤖 AGENT ENGINE (PydanticAI) "]
        Pydantic["PydanticAI Framework"]
        Tools["Tool Calling (@agent.tool)"]
        Groq["Groq API (Low-Latency LLM)"]
    end

    %% Sandbox Execution
    subgraph SANDBOX [" 🔒 SANDBOX EXECUTION LAYER "]
        Docker["Docker Sandbox Driver"]
        DB[(PostgreSQL DB)]
        Plot["Matplotlib Plot (*.png)"]
    end

    %% Workflow
    UI -->|1. Natural Language Query| Pydantic
    Pydantic --> Tools
    Pydantic <--> Groq
    Tools -->|2. Generated Code / SQL| Docker
    Docker -->|Executes Queries| DB
    Docker -->|Generates Chart| Plot
    Plot -->|3. Streamed Chart & Results| UI

    %% Styling
    style USER fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff
    style AGENT fill:#1e1b4b,stroke:#818cf8,stroke-width:2px,color:#fff
    style SANDBOX fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#fff
    style UI fill:#1e293b,stroke:#0284c7,color:#fff
    style Pydantic fill:#312e81,stroke:#6366f1,color:#fff
    style Docker fill:#065f46,stroke:#059669,color:#fff
