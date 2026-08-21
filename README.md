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

```
## 📂 Project Structure
```

.
├── app.py                 # Streamlit UI & Dynamic Media Rendering Engine
├── agent_workflow.py      # Agent Core (PydanticAI Agent, Prompts, Tools)
├── sandbox_driver.py      # Docker Isolation API & Safe Code Execution
├── requirements.txt       # Python Project Dependencies
├── .env.example           # Environment Template (API Keys)
├── .gitignore             # Secrets & Artifact Exclusion Rules
└── README.md              # Project Documentation
```

---

## 🛠️ Tech Stack
---

| Domain | Technology | Description |
| :--- | :--- | :--- |
| **Agentic Framework** | [PydanticAI](https://ai.pydantic.dev/) | Type-safe agent framework for tool calling, validation, and conversation flow. |
| **LLM Provider** | [Groq API](https://groq.com/) | Ultra-fast LLaMA model inference engine for rapid code synthesis. |
| **User Interface** | [Streamlit](https://streamlit.io/) | Interactive chat UI with dynamic artifact rendering. |
| **Sandbox Environment** | [Docker](https://www.docker.com/) | Isolated containerized execution environment for untrusted python scripts. |
| **Database** | [PostgreSQL](https://www.postgresql.org/) | Relational data repository targeted for complex SQL queries. |
| **Data Processing** | Pandas / Matplotlib | Data manipulation, statistical aggregation, and chart plotting. |

---

## 🚀 Quickstart Guide
---

### Prerequisites

- **Python 3.10+**
- **Docker Desktop** installed and running
- **Groq API Key** ([Get your key here](https://console.groq.com/))

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Data-Copilot---Autonomous-AI-Data-Analyst.git
   cd Data-Copilot---Autonomous-AI-Data-Analyst
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=gsk_your_actual_groq_api_key_here
   ```

5. **Run the Application**
   ```bash
   streamlit run app.py
   ```

---

## 📄 License
---
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
---


    style Docker fill:#065f46,stroke:#059669,color:#fff
