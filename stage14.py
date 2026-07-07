import os

def create_files():
    files = {
        "backend/pytest.ini": "[pytest]\nasyncio_mode = auto\nasyncio_default_fixture_loop_scope = function\ntestpaths = tests\n",
        "backend/tests/conftest.py": "import pytest\nfrom app.agents.core.state import SharedContext\n\n@pytest.fixture\ndef mock_context():\n    return SharedContext(original_target=\"https://example.com\", scan_type=\"URL\")\n",
        "backend/tests/unit/test_agents.py": "import pytest\nfrom app.agents.impl.agents import InputValidationAgent, RiskAssessmentAgent\nfrom app.agents.core.state import SharedContext\n\n@pytest.mark.asyncio\nasync def test_input_validation_agent(mock_context):\n    agent = InputValidationAgent()\n    mock_context.original_target = \"https://EXAMPLE.com/path?tracker=123\"\n    \n    result = await agent.execute(mock_context)\n    assert result.normalized_url == \"https://example.com/path\"\n\n@pytest.mark.asyncio\nasync def test_risk_assessment_critical(mock_context):\n    agent = RiskAssessmentAgent()\n    mock_context.threat_intel_flags = [\"Flag 1\"]\n    mock_context.ssl_valid = False\n    mock_context.whois_age_days = 5\n    mock_context.impersonated_brand = \"PayPal\"\n    \n    result = await agent.execute(mock_context)\n    assert result.risk_score == 70.0 # 35 + 15 + 10 + 10\n    assert result.risk_level == \"High\"\n",
        "frontend/vite.config.ts": "import { defineConfig } from 'vite';\nimport react from '@vitejs/plugin-react';\n\nexport default defineConfig({\n  plugins: [react()],\n  test: {\n    environment: 'jsdom',\n    globals: true,\n    setupFiles: './src/tests/setup.ts',\n  }\n});\n",
        "frontend/src/tests/setup.ts": "import '@testing-library/jest-dom';\n",
        "frontend/src/tests/WebsiteScanner.test.tsx": "import React from 'react';\nimport { render, screen, fireEvent } from '@testing-library/react';\nimport WebsiteScanner from '../pages/WebsiteScanner';\nimport { BrowserRouter } from 'react-router-dom';\nimport { vi } from 'vitest';\n\n// Mock Framer Motion to avoid animation issues in jsdom\nvi.mock('framer-motion', () => ({\n  motion: {\n    div: ({ children, ...props }: any) => <div {...props}>{children}</div>,\n  },\n}));\n\ndescribe('WebsiteScanner Component', () => {\n  it('renders correctly', () => {\n    render(<BrowserRouter><WebsiteScanner /></BrowserRouter>);\n    expect(screen.getByText('Website Scanner')).toBeInTheDocument();\n  });\n\n  it('allows typing a URL', () => {\n    render(<BrowserRouter><WebsiteScanner /></BrowserRouter>);\n    const input = screen.getByPlaceholderText('https://example.com');\n    fireEvent.change(input, { target: { value: 'https://test.com' } });\n    expect(input).toHaveValue('https://test.com');\n  });\n});\n"
    }

    for path, content in files.items():
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

if __name__ == "__main__":
    create_files()
    print("Stage 14 Testing Suite Scaffolded.")
