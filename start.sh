#!/bin/bash

# Start the Node.js MCP Server in the background
echo "Starting Node.js MCP Server..."
cd /app/mcp_server
npm start &

# Wait 3 seconds to let the Node server boot up
sleep 3

# Start the Python FastAPI Backend in the foreground
echo "Starting Python FastAPI Backend..."
cd /app/backend
uvicorn app.main:app --host 0.0.0.0 --port 8000
