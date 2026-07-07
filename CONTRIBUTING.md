# Contributing to TrustGuardAI

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
