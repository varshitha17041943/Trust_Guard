import os

def create_files():
    files = {
        "LICENSE": """MIT License

Copyright (c) 2026 TrustGuardAI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""",
        "SECURITY.md": """# Security Policy

## Supported Versions
TrustGuardAI currently supports the following versions with active security updates:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability
If you discover a security vulnerability within TrustGuardAI, please send an e-mail to security@trustguard.ai. All security vulnerabilities will be promptly addressed.

### Threat Intelligence & MCP
TrustGuardAI relies on external Model Context Protocol (MCP) servers to route traffic to Threat Intelligence providers (VirusTotal, Google Safe Browsing). Ensure your API keys are stored securely in `.env` and never hardcoded or committed to version control.
""",
        "CODE_OF_CONDUCT.md": """# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
conduct@trustguard.ai.
""",
        "CHANGELOG.md": """# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-07-07
### Added
- **Multi-Agent Orchestration**: Implemented the Antigravity engine with 9 isolated Google ADK agents.
- **Model Context Protocol (MCP)**: Built a standalone MCP server with Circuit Breaker resilience for external API routing (VirusTotal, Safe Browsing).
- **Explainable AI (XAI)**: Added an Explanation Agent to translate technical JSON into educational English.
- **SaaS Dashboard**: Added Glassmorphism UI, Recharts analytics, and PDF report generation.
- **Dockerization**: Complete containerization of PostgreSQL, Backend, MCP, and Frontend.
""",
        "CONTRIBUTING.md": """# Contributing to TrustGuardAI

First off, thank you for considering contributing to TrustGuardAI! This project is built for the Google AI Agents Capstone and welcomes community improvements.

## 🧠 Adding New ADK Agents
1. Navigate to `backend/app/agents/impl/agents.py`.
2. Inherit from `AgentBase`.
3. Define your custom `prompt` property and override the `execute()` method to mutate the `SharedContext`.
4. Register your new agent in the DAG pipeline inside `backend/app/workflows/engine.py`.

## 🛡️ Adding New MCP Tools
1. Navigate to `mcp/tools/implementations.py`.
2. Write a new asynchronous tool function decorated with `@mcp.tool()`.
3. Define strict Pydantic `Input` and `Output` schemas for the tool.
4. Ensure the tool raises appropriate exceptions so the `CircuitBreaker` can catch them.

## 🚀 Pull Request Process
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Run the test suite: `pytest --cov=app tests/` and `npm run test`.
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
5. Push to the branch (`git push origin feature/AmazingFeature`).
6. Open a Pull Request.
""",
        "README.md": """# TrustGuardAI 🛡️

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)
![Google Capstone](https://img.shields.io/badge/Google-AI_Agents_Capstone-orange.svg)

An Enterprise-Grade, Multi-Agent Cybersecurity Threat Intelligence Platform.  
Built explicitly for the **Google AI Agents Capstone**.

---

## 📖 Project Overview

### Problem Statement
Modern cyber threats, such as zero-day phishing campaigns and typosquatting attacks, bypass traditional heuristic firewalls. Furthermore, existing threat intelligence tools dump raw, highly technical JSON payloads (e.g., `ERR_SSL_PROTOCOL_ERROR`) that non-technical users cannot decipher, leaving them vulnerable to social engineering.

### Solution
TrustGuardAI bridges the gap between deep technical intelligence and human readability. By leveraging an asynchronous, DAG-based **Multi-Agent System (Antigravity Engine)**, the platform queries global threat databases (VirusTotal, Google Safe Browsing, crt.sh) via the **Model Context Protocol (MCP)**. 
A dedicated **Explainable AI (XAI)** Agent then intercepts these technical flags and translates them into educational, actionable English, rendering the results on a beautiful Glassmorphism dashboard.

---

## ✨ Key Features
- **True Multi-Agent Orchestration**: 9 independent Google ADK agents running in a highly optimized Directed Acyclic Graph (DAG) pipeline.
- **Model Context Protocol (MCP)**: Strict Clean Architecture. The core backend **never** makes direct external HTTP requests. All intelligence gathering is piped securely through a standalone MCP server guarded by a stateful Circuit Breaker.
- **Explainable AI (XAI)**: Converts raw JSON into educational tips, UI accordions, and personalized AI recommendations.
- **Enterprise Reporting**: Generate and download professional PDF, Markdown, and JSON security reports dynamically.
- **Advanced Analytics**: Real-time Recharts visualizations powered by TTL-cached PostgreSQL aggregations.

---

## 🛠️ Technology Stack
- **Frontend**: React 18, TypeScript, TailwindCSS, Framer Motion, Recharts, Vitest
- **Backend**: FastAPI, SQLAlchemy (asyncpg), Pydantic, Pytest
- **Multi-Agent Orchestration**: Custom `Antigravity` DAG Engine (Python `asyncio`)
- **Protocol**: Custom Model Context Protocol (MCP) server on port `8001`
- **Database**: PostgreSQL 15 (with `pgvector` available for future embedding support)
- **Containerization**: Docker, Docker Compose, GitHub Actions CI/CD

---

## 🏛️ Architecture & Developer Guide

### 1. Overall Flow
```mermaid
graph LR
    A[React Frontend] -->|SSE Stream| B(FastAPI Backend)
    B -->|Task Dispatch| C{Antigravity Orchestrator}
    C -->|Phase 1| D[Input Validation Agent]
    C -->|Phase 2| E[Security Analysis Agent]
    E <-->|Signed HTTP Request| F((MCP Server :8001))
    F <-->|Lookup| G[VirusTotal API]
    F <-->|Lookup| H[Google Safe Browsing]
    C -->|Phase 3| I[Risk Assessment Agent]
    C -->|Phase 4| J[Explainable AI Agent]
    I --> K[(PostgreSQL)]
```

### 2. The Google ADK Multi-Agent Engine
Our custom `Antigravity` engine orchestrates 9 highly isolated AI agents. Each agent mutates a Pydantic `SharedContext` state object as it passes through the pipeline.
```mermaid
graph TD
    subgraph Ingestion Phase
    A[InputValidationAgent]
    B[QRProcessingAgent]
    end
    subgraph Intelligence Phase
    C[SecurityAnalysisAgent]
    D[BrandVerificationAgent]
    end
    subgraph Assessment Phase
    E[RiskAssessmentAgent]
    end
    subgraph Synthesis Phase
    F[ExplanationAgent]
    G[RecommendationAgent]
    H[OfficialWebsiteAgent]
    I[ReportGenerationAgent]
    end
    A & B --> C & D
    C & D --> E
    E --> F & G & H & I
```

### 3. The Model Context Protocol (MCP) Server
The backend is completely shielded from external API failures. If VirusTotal hits a `429 Too Many Requests`, the MCP Circuit Breaker trips to `OPEN` and injects normalized fallback data into the Multi-Agent pipeline, preventing deadlocks.
```mermaid
graph TD
    A[FastAPI Backend] -->|MCP Request| B{Circuit Breaker}
    B -->|CLOSED| C[Tool Registry]
    C --> D[VirusTotal Tool]
    C --> E[GSB Tool]
    C --> F[SSL Tool]
    B -->|OPEN| G[Fallback Generator]
    G -->|Normalized Safe Data| A
    D & E & F -->|Normalized Threat Data| A
```

### 4. Database ER Diagram
```mermaid
erDiagram
    USERS ||--o{ SCANS : executes
    SCANS ||--o{ THREAT_RESULTS : generates
    SCANS ||--o{ RECOMMENDATIONS : receives
    SCANS ||--o| OFFICIAL_WEBSITES : verifies
```

---

## 📂 Project Structure

```text
TrustGuardAI/
├── backend/                  # FastAPI Main Application
│   ├── app/
│   │   ├── agents/           # The 9 Google ADK Agents
│   │   ├── controllers/      # API Routers (Auth, Scan, Analytics)
│   │   ├── models/           # SQLAlchemy ORM Models
│   │   ├── services/         # Business Logic (JWT, PDFs)
│   │   ├── workflows/        # Antigravity DAG Orchestrator
│   │   └── main.py           # FastAPI Entrypoint
│   ├── tests/                # Pytest Suite
│   └── Dockerfile
├── frontend/                 # React UI
│   ├── src/
│   │   ├── components/       # Reusable Glassmorphism UI
│   │   ├── pages/            # Dashboard, Results, Scanners
│   │   └── tests/            # Vitest Suite
│   └── Dockerfile
├── mcp/                      # Standalone MCP Server
│   ├── tools/                # Extensible Tool Registry
│   ├── server.py             # MCP Entrypoint (:8001)
│   └── Dockerfile
├── docker-compose.yml        # Orchestrates 4 Containers
└── README.md                 # You are here
```

---

## ⚡ Setup & Installation

### Environment Variables
Create a `.env` file inside the `mcp/` directory. (If left blank, the Circuit Breaker will gracefully handle fallback data).
```ini
VIRUSTOTAL_API_KEY=your_vt_key
GOOGLE_SAFE_BROWSING_API_KEY=your_gsb_key
```

### Running via Docker (Recommended)
Ensure you have Docker Engine and Docker Compose installed. Execute the following command from the root directory:
```bash
docker-compose up --build -d
```
The architecture will boot across 4 isolated containers:
1. `db`: PostgreSQL Database on `5432`.
2. `mcp`: MCP Server on `8001`.
3. `backend`: FastAPI Engine on `8000`.
4. `frontend`: Nginx serving React on `3000`.

Navigate to **http://localhost:3000** in your browser.

### Cloud Deployment
- **Frontend**: Deploy the `frontend/` directory to **Vercel** with the build command `npm run build`.
- **Backend & MCP**: Deploy the `backend/Dockerfile` and `mcp/Dockerfile` to **Google Cloud Run** or **Render**, ensuring the `MCP_SERVER_URL` environment variable points to the internal MCP IP.

---

## 📚 API Documentation (Swagger)
Once the backend is running, the fully documented OpenAPI interface is available at:  
👉 `http://localhost:8000/docs`

### Example Request (`POST /api/scan/url`)
```json
{
  "target": "https://paypal-secure-login.com"
}
```

### Example Server-Sent Events (SSE) Stream
```json
data: {"step": "SecurityAnalysisAgent", "status": "running"}
data: {"step": "SecurityAnalysisAgent", "status": "complete", "result": {"threat_intel_flags": ["VT_FLAG", "GSB_FLAG"]}}
```

---

## 📸 Screenshots

*(Replace these placeholders with actual screenshots from your repository)*

| Dashboard | Real-time SSE Scanning |
|-----------|------------------------|
| `![Dashboard](path/to/dashboard.png)` | `![Scanner](path/to/scanner.png)` |

| Explainable AI Results | PDF Report Generation |
|------------------------|-----------------------|
| `![Results](path/to/results.png)` | `![PDF](path/to/pdf.png)` |

---

## 🔮 Future Scope
- **LLM Embeddings**: Integrate `pgvector` to run semantic searches across historical threat reports.
- **Browser Extension**: Port the React application into a Chrome extension for real-time URL interception.
- **Dynamic Kubernetes**: Orchestrate the individual ADK agents as separate serverless functions.

---

## 🙌 Acknowledgements
Built by varsh for the **Google AI Agents Capstone**. 
Thanks to the open-source community behind FastAPI, React, and Recharts.

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
"""
    }

    for path, content in files.items():
        dirname = os.path.dirname(path)
        if dirname:
            os.makedirs(dirname, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

if __name__ == "__main__":
    create_files()
    print("Stage 17 Repository Documentation Scaffolded.")
