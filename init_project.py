import os

def create_directories():
    dirs = [
        ".github/workflows",
        "docs",
        "docker",
        "scripts",
        "mcp/tests",
        "mcp/config",
        "mcp/tools",
        "frontend/public",
        "frontend/src/assets",
        "frontend/src/components",
        "frontend/src/contexts",
        "frontend/src/hooks",
        "frontend/src/layouts",
        "frontend/src/pages",
        "frontend/src/services",
        "frontend/src/types",
        "frontend/src/utils",
        "frontend/tests",
        "backend/app/agents",
        "backend/app/workflows",
        "backend/app/database",
        "backend/app/config",
        "backend/app/services",
        "backend/app/utils",
        "backend/tests"
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        # Create a .gitkeep to ensure the folder is tracked
        with open(os.path.join(d, ".gitkeep"), "w") as f:
            pass

def create_files():
    files = {
        "README.md": "# TrustGuardAI\n\nProduction-grade Multi-Agent Fake Website Detection System.\n\n## Structure\n- `frontend/`: React + Vite\n- `backend/`: FastAPI\n- `mcp/`: Model Context Protocol Server\n- `docker/`: Docker configurations\n- `docs/`: Documentation\n",
        ".gitignore": "node_modules/\n__pycache__/\n*.pyc\n.env\n.env.*\n!.env.example\ndist/\nbuild/\n.DS_Store\ncoverage/\n",
        ".env.example": "POSTGRES_USER=postgres\nPOSTGRES_PASSWORD=postgres\nPOSTGRES_DB=trustguard\nDATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/trustguard\nSECRET_KEY=supersecretkey\nENVIRONMENT=development\nMCP_API_KEY=mcp_secret\n",
        "docker-compose.yml": "version: '3.8'\n\nservices:\n  db:\n    image: pgvector/pgvector:pg15\n    environment:\n      POSTGRES_USER: ${POSTGRES_USER:-postgres}\n      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-postgres}\n      POSTGRES_DB: ${POSTGRES_DB:-trustguard}\n    volumes:\n      - postgres_data:/var/lib/postgresql/data\n    ports:\n      - \"5432:5432\"\n    restart: always\n\n  backend:\n    build:\n      context: ./backend\n      dockerfile: Dockerfile\n    environment:\n      - DATABASE_URL=${DATABASE_URL}\n      - SECRET_KEY=${SECRET_KEY}\n    depends_on:\n      - db\n    ports:\n      - \"8000:8000\"\n    restart: always\n\n  mcp:\n    build:\n      context: ./mcp\n      dockerfile: Dockerfile\n    environment:\n      - MCP_API_KEY=${MCP_API_KEY}\n    ports:\n      - \"8001:8000\"\n    restart: always\n\n  frontend:\n    build:\n      context: ./frontend\n      dockerfile: Dockerfile\n    ports:\n      - \"3000:80\"\n    depends_on:\n      - backend\n    restart: always\n\nvolumes:\n  postgres_data:\n",
        "docker/backend.Dockerfile": "FROM python:3.11-slim\nWORKDIR /app\nCOPY requirements.txt .\nRUN pip install --no-cache-dir -r requirements.txt\nCOPY . .\nCMD [\"uvicorn\", \"app.main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]\n",
        "docker/frontend.Dockerfile": "FROM node:20-alpine AS build\nWORKDIR /app\nCOPY package*.json ./\nRUN npm install\nCOPY . .\nRUN npm run build\n\nFROM nginx:alpine\nCOPY --from=build /app/dist /usr/share/nginx/html\nEXPOSE 80\nCMD [\"nginx\", \"-g\", \"daemon off;\"]\n",
        "docker/mcp.Dockerfile": "FROM python:3.11-slim\nWORKDIR /app\nCOPY requirements.txt .\nRUN pip install --no-cache-dir -r requirements.txt\nCOPY . .\nCMD [\"uvicorn\", \"server:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]\n",
        "backend/requirements.txt": "fastapi\nuvicorn\nsqlalchemy\nasyncpg\npgvector\nalembic\npydantic\npydantic-settings\npython-jose[cryptography]\npasslib[bcrypt]\npython-multipart\nhit-trustguard-adk\npytest\n",
        "backend/app/main.py": "from fastapi import FastAPI\n\napp = FastAPI(title=\"TrustGuardAI Backend API\", description=\"Backend services for TrustGuardAI.\")\n\n@app.get(\"/\")\nasync def root():\n    return {\"message\": \"Welcome to TrustGuardAI Backend\"}\n\n@app.get(\"/health\")\nasync def health():\n    return {\"status\": \"ok\"}\n",
        "frontend/package.json": "{\n  \"name\": \"trustguard-frontend\",\n  \"version\": \"1.0.0\",\n  \"type\": \"module\",\n  \"scripts\": {\n    \"dev\": \"vite\",\n    \"build\": \"tsc && vite build\",\n    \"lint\": \"eslint . --ext ts,tsx --report-unused-disable-directives --max-warnings 0\",\n    \"preview\": \"vite preview\",\n    \"format\": \"prettier --write \\\"src/**/*.{ts,tsx,css}\\\"\"\n  },\n  \"dependencies\": {\n    \"react\": \"^18.2.0\",\n    \"react-dom\": \"^18.2.0\",\n    \"react-router-dom\": \"^6.22.3\",\n    \"axios\": \"^1.6.8\",\n    \"framer-motion\": \"^11.0.14\"\n  },\n  \"devDependencies\": {\n    \"@types/react\": \"^18.2.64\",\n    \"@types/react-dom\": \"^18.2.21\",\n    \"@typescript-eslint/eslint-plugin\": \"^7.1.1\",\n    \"@typescript-eslint/parser\": \"^7.1.1\",\n    \"@vitejs/plugin-react\": \"^4.2.1\",\n    \"eslint\": \"^8.57.0\",\n    \"eslint-plugin-react-hooks\": \"^4.6.0\",\n    \"eslint-plugin-react-refresh\": \"^0.4.5\",\n    \"prettier\": \"^3.2.5\",\n    \"typescript\": \"^5.2.2\",\n    \"vite\": \"^5.1.6\",\n    \"tailwindcss\": \"^3.4.1\",\n    \"postcss\": \"^8.4.35\",\n    \"autoprefixer\": \"^10.4.18\"\n  }\n}\n",
        "frontend/tailwind.config.js": "/** @type {import('tailwindcss').Config} */\nexport default {\n  content: [\n    \"./index.html\",\n    \"./src/**/*.{js,ts,jsx,tsx}\",\n  ],\n  theme: {\n    extend: {\n      colors: {\n        primary: \"#0f172a\",\n        secondary: \"#1e293b\",\n        accent: \"#38bdf8\"\n      }\n    },\n  },\n  plugins: [],\n}\n",
        "frontend/postcss.config.js": "export default {\n  plugins: {\n    tailwindcss: {},\n    autoprefixer: {},\n  },\n}\n",
        "frontend/tsconfig.json": "{\n  \"compilerOptions\": {\n    \"target\": \"ES2020\",\n    \"useDefineForClassFields\": true,\n    \"lib\": [\"ES2020\", \"DOM\", \"DOM.Iterable\"],\n    \"module\": \"ESNext\",\n    \"skipLibCheck\": true,\n    \"moduleResolution\": \"bundler\",\n    \"allowImportingTsExtensions\": true,\n    \"resolveJsonModule\": true,\n    \"isolatedModules\": true,\n    \"noEmit\": true,\n    \"jsx\": \"react-jsx\",\n    \"strict\": true,\n    \"noUnusedLocals\": true,\n    \"noUnusedParameters\": true,\n    \"noFallthroughCasesInSwitch\": true\n  },\n  \"include\": [\"src\"],\n  \"references\": [{ \"path\": \"./tsconfig.node.json\" }]\n}\n",
        "frontend/tsconfig.node.json": "{\n  \"compilerOptions\": {\n    \"composite\": true,\n    \"skipLibCheck\": true,\n    \"module\": \"ESNext\",\n    \"moduleResolution\": \"bundler\",\n    \"allowSyntheticDefaultImports\": true\n  },\n  \"include\": [\"vite.config.ts\"]\n}\n",
        "frontend/.eslintrc.json": "{\n  \"root\": true,\n  \"env\": { \"browser\": true, \"es2020\": true },\n  \"extends\": [\n    \"eslint:recommended\",\n    \"plugin:@typescript-eslint/recommended\",\n    \"plugin:react-hooks/recommended\"\n  ],\n  \"ignorePatterns\": [\"dist\", \".eslintrc.cjs\"],\n  \"parser\": \"@typescript-eslint/parser\",\n  \"plugins\": [\"react-refresh\"],\n  \"rules\": {\n    \"react-refresh/only-export-components\": [\n      \"warn\",\n      { \"allowConstantExport\": true }\n    ]\n  }\n}\n",
        "frontend/.prettierrc": "{\n  \"semi\": true,\n  \"singleQuote\": true,\n  \"tabWidth\": 2,\n  \"trailingComma\": \"es5\",\n  \"printWidth\": 100\n}\n",
        "frontend/vite.config.ts": "import { defineConfig } from 'vite'\nimport react from '@vitejs/plugin-react'\n\nexport default defineConfig({\n  plugins: [react()],\n  server: {\n    port: 3000,\n  },\n})\n",
        "frontend/index.html": "<!doctype html>\n<html lang=\"en\">\n  <head>\n    <meta charset=\"UTF-8\" />\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />\n    <title>TrustGuardAI</title>\n  </head>\n  <body>\n    <div id=\"root\"></div>\n    <script type=\"module\" src=\"/src/main.tsx\"></script>\n  </body>\n</html>\n",
        "frontend/src/main.tsx": "import React from 'react'\nimport ReactDOM from 'react-dom/client'\nimport App from './App.tsx'\nimport './index.css'\n\nReactDOM.createRoot(document.getElementById('root')!).render(\n  <React.StrictMode>\n    <App />\n  </React.StrictMode>,\n)\n",
        "frontend/src/App.tsx": "import React from 'react';\n\nfunction App() {\n  return (\n    <div className=\"min-h-screen bg-primary text-white flex items-center justify-center\">\n      <h1 className=\"text-4xl font-bold text-accent\">TrustGuardAI Initialized</h1>\n    </div>\n  );\n}\n\nexport default App;\n",
        "frontend/src/index.css": "@tailwind base;\n@tailwind components;\n@tailwind utilities;\n",
        ".github/workflows/ci.yml": "name: CI/CD\n\non:\n  push:\n    branches: [ \"main\" ]\n  pull_request:\n    branches: [ \"main\" ]\n\njobs:\n  build:\n    runs-on: ubuntu-latest\n    steps:\n    - uses: actions/checkout@v3\n    - name: Set up Node.js\n      uses: actions/setup-node@v3\n      with:\n        node-version: '20'\n    - name: Install Frontend Dependencies\n      run: cd frontend && npm install\n    - name: Lint Frontend\n      run: cd frontend && npm run lint\n    - name: Set up Python\n      uses: actions/setup-python@v4\n      with:\n        python-version: '3.11'\n    - name: Install Backend Dependencies\n      run: cd backend && pip install -r requirements.txt\n    - name: Test Backend\n      run: cd backend && pytest\n"
    }

    for path, content in files.items():
        os.makedirs(os.path.dirname(path) if os.path.dirname(path) else ".", exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

if __name__ == "__main__":
    create_directories()
    create_files()
    print("Project initialized successfully.")
