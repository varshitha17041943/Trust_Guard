import os

def create_files():
    files = {
        "docs/CAPSTONE_EVALUATION.md": """# TrustGuardAI: Google AI Agents Capstone Evaluation Guide

Welcome Judges! This document is specifically curated to help you evaluate **TrustGuardAI** against the core criteria of the Google AI Agents Capstone. 

Our architecture completely abandons legacy monolithic backends in favor of a modern **Multi-Agent Collaboration** ecosystem powered by the **Model Context Protocol (MCP)** and our custom **Antigravity Workflow Engine**.

---

## 🌟 Why We Built a Multi-Agent System (Instead of a Monolith)

In traditional cybersecurity tools, a single backend controller tries to handle URL parsing, SSL verification, threat intelligence lookups, risk scoring, and report generation simultaneously. This leads to:
1. **Brittle Code**: Changing the VT API breaks the PDF generator.
2. **Slow Execution**: Synchronous blocking prevents parallel intelligence gathering.
3. **Hallucinations**: Using a single LLM to perform rigid math, parse JSON, and generate creative text results in massive hallucination rates.

**The Solution:**
By breaking the problem down into **9 highly specialized, mathematically restricted Google ADK Agents**, we achieve:
- **Parallelism**: Multiple agents query different databases asynchronously.
- **Strict Role Boundaries**: The `RiskAssessmentAgent` is restricted to rigid mathematics. It cannot invent data. The `ExplanationAgent` is restricted to Natural Language Processing (NLP) and cannot alter the risk score.
- **Resilience**: If the `BrandVerificationAgent` fails, the `Antigravity` engine logs the error and continues the pipeline, rather than crashing the entire scan.

---

## 🤖 The 9 Google ADK Agents: Detailed Breakdown

Each agent operates on a shared `SharedContext` Pydantic state, but has strictly isolated responsibilities.

### 1. Input Validation Agent
- **Purpose**: Sanitizes untrusted user input.
- **Input**: Raw URL string (`https://PAYPAL.com/login?tracker=123`).
- **Output**: Normalized URL (`https://paypal.com/login`).
- **Responsibilities**: Prevents SQL injection and directory traversal attacks before they hit the intelligence gathering phase.

### 2. QR Processing Agent
- **Purpose**: Validates base64 QR uploads and safely extracts malicious embedded links.
- **Responsibilities**: Acts as a bridge between the physical world and the digital scanner.

### 3. Security Analysis Agent
- **Purpose**: The core investigator. It communicates with global threat databases.
- **Tools**: Strictly limited to `MCPClient`. It **cannot** use raw HTTP.
- **Responsibilities**: Dispatches parallel MCP calls to VirusTotal and Google Safe Browsing. Appends `threat_intel_flags` to the state.

### 4. Brand Verification Agent
- **Purpose**: Detects Typosquatting (e.g., `paypa1.com`).
- **Output**: Sets the `impersonated_brand` flag.

### 5. Risk Assessment Agent
- **Purpose**: The mathematical brain. 
- **Responsibilities**: Ingests all previous flags and calculates a strict 0-100 `risk_score` using a deterministic weighting algorithm (30% Threat Intel, 15% SSL, 10% Typosquatting).

### 6. Explanation Agent (Explainable AI - XAI)
- **Purpose**: Enhances user trust by removing technical jargon.
- **Input**: `ssl_valid == False`.
- **Output**: "This website doesn't use a secure encrypted connection."

### 7. Recommendation Agent
- **Purpose**: Generates personalized, actionable directives (e.g., "Do Not Share OTP").

### 8. Official Website Agent
- **Purpose**: If Typosquatting is detected, it dynamically searches for and provides the true, verified domain to protect the user.

### 9. Report Generation Agent
- **Purpose**: Aggregates the final `SharedContext` state and commits the immutable ledger to PostgreSQL.

---

## 🛡️ How MCP Increases Security & Reliability

The **Model Context Protocol (MCP)** completely isolates our AI agents from the chaotic external internet. 

In TrustGuardAI, the backend API runs on port `8000`, and the MCP Server runs on port `8001`. 
- **No Direct Access**: Agents are physically blocked from running `requests.get()`. They must dispatch a signed request to the MCP server.
- **Stateful Circuit Breaker**: If VirusTotal goes down, the MCP Circuit Breaker trips to `OPEN`. Instead of hanging the agent, MCP instantly returns a normalized fallback object. The Agent continues running flawlessly!

```mermaid
sequenceDiagram
    participant Agent as Security Analysis Agent
    participant MCP as MCP Server
    participant VT as VirusTotal API
    
    Agent->>MCP: execute_tool("virustotal_lookup", url)
    MCP->>VT: HTTP GET /api/v3/domains
    VT--xMCP: 429 Too Many Requests (Rate Limit)
    Note over MCP: Circuit Breaker TRIPS to OPEN!
    MCP-->>Agent: Returns normalized fallback {malicious: 0}
    Note over Agent: Agent continues without crashing!
```

---

## 🚀 How Antigravity Improves Orchestration

Our custom **Antigravity Engine** replaces rigid `while` loops with a highly optimized Directed Acyclic Graph (DAG) running on Python's `asyncio`.

- **Asynchronous Execution**: Agents in the same phase (e.g., Intelligence Phase) run concurrently using `asyncio.gather()`.
- **Server-Sent Events (SSE)**: As each agent completes its task, Antigravity yields an SSE chunk directly to the React frontend, allowing the user to watch the multi-agent collaboration happen in real-time on their dashboard!

```mermaid
graph TD
    subgraph Antigravity Engine Flow
    A[Start SSE Stream] --> B(Ingestion Phase)
    B --> C(Intelligence Phase: Parallel Agents)
    C --> D(Assessment Phase)
    D --> E(Synthesis Phase)
    E --> F[Close Stream]
    end
```

---

## 🤝 Explainable AI (XAI) and Trust

In cybersecurity, trust is paramount. A user will not trust an AI that simply says "Risk Score: 90". 

Our **Explainable AI (XAI)** module directly addresses this. By enforcing that the `ExplanationAgent` strictly maps technical flags to highly curated, educational JSON dictionaries (including real-world examples and prevention tips), we ensure that TrustGuardAI is not just an analysis tool, but a **cybersecurity education platform**.

Thank you for reviewing TrustGuardAI!
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
    print("Capstone Docs Scaffolded.")
