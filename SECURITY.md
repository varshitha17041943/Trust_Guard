# Security Policy

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
