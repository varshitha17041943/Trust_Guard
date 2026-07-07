# TrustGuardAI: 5-Minute Capstone Demonstration Script

**Total Estimated Time:** 5:00
**Target Audience:** Google AI Agents Capstone Judges
**Core Themes to Highlight:** Innovation, Technical Depth (MCP & DAG Orchestration), Practical Impact (XAI).

---

## 🎬 Part 1: Problem Statement (0:00 - 0:30)
**Slide Visual:** Dark background, stark text. "The Threat Landscape: Zero-Day Phishing & Typosquatting." A graphic showing a fake PayPal login page next to a real one.
**Transition Cue:** Fade in.

**Narration / Speaker Notes:**
"Hello everyone, and welcome to TrustGuardAI. Today, cyber threats like zero-day phishing campaigns and typosquatting bypass traditional heuristic firewalls with ease. Furthermore, existing threat intelligence tools dump raw, highly technical JSON payloads that everyday users simply cannot decipher. They might see a flag that says 'ERR_SSL_PROTOCOL_ERROR' and ignore it, falling victim to social engineering. We need a system that doesn't just scan for threats, but actively translates them into actionable intelligence."

---

## 💡 Part 2: Solution Overview (0:30 - 0:50)
**Slide Visual:** The TrustGuardAI logo. Three pillars appear: "Multi-Agent System", "Model Context Protocol", "Explainable AI".
**Transition Cue:** Slide in from right.

**Narration / Speaker Notes:**
"Enter TrustGuardAI. We abandoned the legacy monolithic backend approach. Instead, we built a Next-Generation security scanner powered by a robust **Multi-Agent Collaboration** ecosystem. By leveraging the Google ADK, the Model Context Protocol, and a custom Antigravity workflow engine, we actively parse global intelligence databases and translate those findings into beautiful, human-readable safety dashboards."

---

## 🏛️ Part 3: Architecture & Google ADK Agents (0:50 - 1:45)
**Slide Visual:** The 9-Agent DAG Topology Mermaid diagram. Highlight the isolated roles (Ingestion, Intelligence, Assessment, Synthesis).
**Transition Cue:** Crossfade to architecture diagram.

**Narration / Speaker Notes:**
"Let's look under the hood. Why use multiple agents? If we asked a single LLM to perform rigid math, parse JSON, and generate creative text, the hallucination rate would skyrocket. 

Instead, our custom **Antigravity engine** orchestrates **9 highly specialized Google ADK Agents**. 
- The *Security Analysis Agent* operates purely in the intelligence phase.
- The *Risk Assessment Agent* is restricted to a rigid, deterministic mathematical weighting algorithm. It cannot invent data.
- The *Explanation Agent* focuses entirely on Natural Language Processing to generate user trust.

These agents run asynchronously in a Directed Acyclic Graph, meaning we can execute parallel database lookups without blocking the main thread."

---

## 🛡️ Part 4: The Model Context Protocol (MCP) (1:45 - 2:15)
**Slide Visual:** MCP Circuit Breaker diagram. Show the isolated port 8001 server and the fallback generator.
**Transition Cue:** Zoom into the "Intelligence Phase" of the previous diagram.

**Narration / Speaker Notes:**
"But how do we safely connect these agents to the outside world? Through strict **Clean Architecture** using the Model Context Protocol (MCP). 

Our core backend API *never* makes a direct HTTP request to the internet. Instead, agents dispatch signed requests to a completely isolated MCP Server running on a separate port. This MCP server features a stateful **Circuit Breaker**. If a global database like VirusTotal rate-limits us, the Circuit Breaker trips to OPEN, intercepting the request and returning a normalized fallback object. Our agents never crash, and the system never deadlocks. This is enterprise-grade reliability."

---

## 💻 Part 5: Live Demo (2:15 - 4:15)
**Screen Recording Visual:** Switch to screen share of the `localhost:3000` React frontend. Dark mode Glassmorphism UI.
**Transition Cue:** Screen share transition.

**Narration / Speaker Notes:**
*(0:00 - 0:30 of Demo)* 
"Let's see it in action. I'm going to scan a known malicious typosquatted domain: `paypal-secure-login.com`. Watch the UI carefully."
*(Click Scan. Point out the SSE real-time streaming).* 
"Because our Antigravity engine uses Server-Sent Events, you can literally watch the 9 ADK Agents hand off the `SharedContext` state to each other in real-time. No loading spinners, just raw, live orchestration."

*(0:30 - 1:15 of Demo)*
"Here is the final **Explainable AI (XAI)** dashboard. Notice how there is no raw JSON? The Explanation Agent intercepted the technical flags from the MCP server and translated them into these educational accordions. 
Our Recommendation Agent noticed the Critical Risk Level and immediately issued a 'Close Tab Immediately' directive. And because it detected the 'PayPal' typosquat, the Official Website Agent dynamically provided the true, verified domain to protect the user."

*(1:15 - 2:00 of Demo)*
"Finally, for enterprise compliance, we can click 'Download PDF'. Our backend `ReportService` bypasses bulky headless browsers and dynamically paints a beautiful, native Python PDF document containing all of our AI recommendations."

---

## 🚀 Part 6: Deployment & Future Scope (4:15 - 5:00)
**Slide Visual:** Docker logos, GitHub Actions CI/CD pipeline, and bullet points for future scope (`pgvector` embeddings).
**Transition Cue:** Fade back to slide deck.

**Narration / Speaker Notes:**
"TrustGuardAI is 100% production-ready. The entire stack—the React frontend, the FastAPI backend, the MCP server, and the PostgreSQL database—orchestrates seamlessly via Docker Compose. We have enforced strict JWT HttpOnly cookie security, and our GitHub Actions pipeline guarantees zero broken deployments.

For the future, we plan to leverage PostgreSQL's `pgvector` to allow our agents to run semantic similarity searches across historical threat reports.

TrustGuardAI demonstrates that by combining Google ADK Agents, the Model Context Protocol, and Explainable AI, we can build systems that don't just detect threats—they educate and protect the user. Thank you."
