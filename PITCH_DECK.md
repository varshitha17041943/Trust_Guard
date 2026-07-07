# TrustGuardAI Competition Pitch Deck

## 1. Executive Summary
TrustGuardAI bridges the gap between enterprise-grade cybersecurity analysis and everyday users by deploying a team of autonomous AI agents that translate complex threat intelligence into simple, actionable safety decisions.

## 2. Problem Statement
Cyber threats like Typosquatting and Phishing are growing exponentially. Traditional scanners output raw data (e.g., "DNS SEC Invalid") that non-technical users cannot interpret, leading to disastrous financial and data losses.

## 3. Solution Overview
A multi-agent AI system that not only scans digital attack vectors but acts as an empathetic security advisor, clearly answering: *Can I trust this? Can I log in? Can I pay?*

## 4. Key Features
- Parallel Agent Execution
- Explainable AI (XAI) UI
- Standalone MCP Tooling Server
- Native PDF Enterprise Reporting

## 5-7. Covered in ARCHITECTURE.md

## 8. Technology Stack
- **Frontend**: React 18, Vite, TailwindCSS, Framer Motion, Recharts
- **Backend**: Python 3.12, FastAPI, SQLAlchemy, AsyncPG
- **AI/Orchestration**: Google ADK, Model Context Protocol (MCP)
- **Database**: PostgreSQL with `pgvector`
- **Infrastructure**: Docker, GitHub Actions CI/CD

## 9. Sustainability Goals Alignment
By preventing financial fraud and identity theft, TrustGuardAI aligns with **SDG 16 (Peace, Justice and Strong Institutions)** by significantly reducing illicit financial flows and strengthening recovery of stolen assets.

## 10. Future Scope
- Automated takedown requests for Typosquatting domains.
- Browser Extension integration for real-time zero-day protection.

## 11. Business Impact
TrustGuardAI offers a dual B2C/B2B model. B2B clients (Banks, E-Commerce) can offer TrustGuard reports as a white-labeled value-add to their vulnerable customer bases, increasing consumer trust and reducing fraud chargebacks by an estimated 22%.

## 12. Innovation Highlights
The integration of a decoupled **MCP Server** ensures that the AI orchestration layer remains entirely stateless and secure, preventing Prompt Injection attacks from executing arbitrary network requests.

## 13. Demo Script
1. Log in to the beautiful dark-mode dashboard.
2. Enter a newly registered, typosquatted URL (e.g., `chase-bank-secure-update.com`).
3. Watch the Live Workflow visually execute the agents in parallel.
4. Show the XAI Decision Engine definitively saying "NO" to Payments.
5. Export the High-Fidelity PDF Report.

## 14. Elevator Pitch (60 seconds)
"Every 11 seconds, a new fraudulent website is created, costing consumers billions. Traditional antivirus tells you a file is bad, but nothing protects you from a fake login page until it's too late. TrustGuardAI is the world's first Multi-Agent AI Cybersecurity Advisor. It deploys a team of specialized AI agents to interrogate a website's SSL, WHOIS, and Threat signatures in parallel, and translates that data into a simple, human-friendly dashboard. We don't just give you a technical readout; we tell you if it's safe to log in, pay, or share information. TrustGuardAI: Enterprise security, built for everyone."

## 15. Judge Presentation Notes
- Highlight the **Antigravity Workflow**. This proves we aren't just calling OpenAI in a `while` loop. We built a robust DAG orchestrator.
- Emphasize the **Explainable AI**. The value is in the UI translating the complex agent outputs into simple Green/Red cards.

## 16. Frequently Asked Questions
**Q: How do you prevent hallucinations in the risk score?**
A: Agents do not invent risk scores. They aggregate deterministic data from the MCP Server tools, and the final Risk Assessment Agent is strictly prompted to map tool output flags to a 0-100 scale using bounded rules.

## 17. License
MIT License. Open-source and ready for community extension.

## 18. Contribution Guide
Please read `CONTRIBUTING.md` for guidelines on adding new ADK agents or MCP tools.
