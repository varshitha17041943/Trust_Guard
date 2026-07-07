# TrustGuardAI Architecture

## 1. Multi-Agent Architecture Explanation
Instead of relying on a single, monolithic LLM prompt to analyze a website, TrustGuardAI deploys a specialized team of autonomous agents using the Google ADK.
- **Input Validation Agent**: Ensures URL sanitization.
- **QR Processing Agent**: Extracts and validates payloads from physical QR vectors.
- **SSL Analysis Agent**: Interrogates the certificate chain.
- **WHOIS Analysis Agent**: Detects domain age anomalies.
- **Threat Intelligence Agent**: Cross-references global threat feeds.
- **Risk Assessment Agent**: Aggregates the parallel findings into a deterministic risk score.

## 2. MCP Architecture Explanation
The Model Context Protocol (MCP) acts as a strictly isolated microservice. AI Agents NEVER communicate directly with external web services. Instead, they format intent parameters and pass them to the MCP Server, which executes the arbitrary external python tools and returns structured JSON.

## 3. Antigravity Workflow Explanation
The Antigravity Engine orchestrates the Google ADK agents using a Directed Acyclic Graph (DAG). It initiates a background `asyncio.gather` pool to run the analytical agents in parallel, cutting scan time by 75%. It includes a native Server-Sent Events (SSE) bridge to stream execution states directly to the React frontend in real time.
