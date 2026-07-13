---
name: trustguard_analyst
description: Equips the Antigravity Agent with the ability to autonomously query and analyze the local TrustGuardAI threat database.
---
# 🛡️ TrustGuardAI Analyst Skill
**Custom Agentic Skill for the ADK Framework**
This skill teaches the autonomous agent (Antigravity) how to interact with the underlying database of the TrustGuardAI platform. By utilizing this skill, the agent can autonomously retrieve, analyze, and format real-time cybersecurity scan data for the user without requiring a dedicated API endpoint.
## 🎯 Purpose & Triggers
- **Trigger:** Activate this skill whenever the user asks for historical scan data, threat summaries, or database metrics.
- **Goal:** Provide the agent with the necessary SQL schema and execution environment to query the `trustguard.db` securely.
## 🗄️ Database Architecture
The agent must query the local SQLite database located at `backend/trustguard.db`.
The core schema consists of two primary tables:
### 1. `scans` Table
Records the overarching metadata of a threat analysis.
- `id` (INTEGER PRIMARY KEY)
- `target` (VARCHAR): The URL analyzed
- `risk_score` (FLOAT): 0-100 severity score
- `risk_level` (VARCHAR): Low, Medium, High, or Critical
### 2. `threat_results` Table
Records the specific flags triggered by the Multi-Agent Swarm (e.g., `SecurityAnalysisAgent`).
- `scan_id` (INTEGER): Foreign key to `scans`
- `agent_name` (VARCHAR): The ADK agent that flagged the threat
- `description` (TEXT): The threat explanation
---
## 🛠️ Execution Instructions
When utilizing this skill, the agent must adhere to the following workflow:
1. **Script Execution:** Do NOT use the raw `sqlite3` CLI tool. Instead, autonomously write and execute a Python script utilizing `pandas` for dataframe manipulation.
2. **Data Formatting:** ALWAYS format the retrieved output into a clean GitHub-Flavored Markdown (GFM) table for the user.
3. **Threat Highlighting:** Utilize GitHub Alerts (e.g., `> [!WARNING]`) to explicitly highlight any scans that returned a `Critical` or `High` risk level.




## 🐍 Reference Implementation
The agent may use the following Python reference snippet to bootstrap the query:

```python
import sqlite3
import pandas as pd

def analyze_recent_threats():
    conn = sqlite3.connect('backend/trustguard.db')
    query = """
        SELECT s.target, s.risk_score, s.risk_level, t.agent_name, t.description 
        FROM scans s
        LEFT JOIN threat_results t ON s.id = t.scan_id
        ORDER BY s.created_at DESC LIMIT 5
    """
    df = pd.read_sql_query(query, conn)
    print(df.to_markdown())
    conn.close()

analyze_recent_threats()
```
