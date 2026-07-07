# TrustGuardAI: Capstone Abstract

**Project Title**: TrustGuardAI
**Category**: AI Cybersecurity / Multi-Agent Systems
**Core Technology**: Google ADK, FastAPI, React, PostgreSQL (pgvector), MCP

## One-Page Abstract
TrustGuardAI is a next-generation cybersecurity platform designed to protect users from sophisticated Zero-Day phishing campaigns, Typosquatting, and malicious QR codes. Traditional security tools output raw, highly technical JSON payloads that confuse non-technical users, leaving them vulnerable to social engineering.

TrustGuardAI solves this by deploying a sophisticated **Multi-Agent System (9 Google ADK Agents)** orchestrated by a custom Directed Acyclic Graph (DAG) engine called **Antigravity**. Instead of relying on a monolithic, hallucination-prone backend, each agent has a strictly isolated responsibility (e.g., Risk Assessment is isolated to rigid mathematics, Explanation is isolated to NLP).

To guarantee enterprise security and prevent deadlocks, the core backend never directly queries the internet. Instead, it relies on the **Model Context Protocol (MCP)**. All external threat intelligence (VirusTotal, Google Safe Browsing) is piped through a standalone MCP server guarded by a stateful Circuit Breaker.

Finally, an **Explainable AI (XAI)** module translates all technical findings into beautifully formatted, educational UI components, empowering users to understand *why* a threat is dangerous, not just *that* it is dangerous.

**Impact**: TrustGuardAI bridges the gap between deep technical intelligence and human readability, transforming a standard URL scanner into a proactive cybersecurity education platform.
