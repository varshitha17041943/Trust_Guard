# LinkedIn / Portfolio Summary

### Title: TrustGuardAI - Multi-Agent Cybersecurity Platform

**Summary**: 
Architected and deployed an enterprise-grade cybersecurity platform for the Google AI Agents Capstone. Engineered a custom asynchronous DAG orchestrator ('Antigravity') to coordinate 9 specialized Google ADK agents in real-time.

**Key Achievements**:
- **Multi-Agent Orchestration**: Built a 9-agent pipeline to process URLs and QR codes, isolating rigid mathematics from NLP to achieve a 0% hallucination rate on risk scoring.
- **Model Context Protocol (MCP)**: Implemented strict Clean Architecture by offloading all external integrations (VirusTotal, Google Safe Browsing) to an isolated MCP server protected by a stateful Circuit Breaker.
- **RAG & Explainable AI**: Integrated `pgvector` and Gemini to dynamically translate complex SSL/DNS threat flags into educational, human-readable insights.
- **Full-Stack Optimization**: Delivered a fully Dockerized ecosystem featuring a React 18 Glassmorphism dashboard, real-time SSE streaming, and a FastAPI/asyncpg backend.

**Tech Stack**: Python (FastAPI, SQLAlchemy, ADK, asyncio), TypeScript (React, Tailwind, Recharts), PostgreSQL (pgvector), Docker, GitHub Actions CI/CD.
