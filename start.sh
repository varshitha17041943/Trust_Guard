#!/bin/bash

# Start the Python MCP Server in the background on port 3001
echo "Starting Python MCP Server..."
cd /app/mcp
uvicorn server:app --host 0.0.0.0 --port 3001 &

# Wait 3 seconds to let the MCP server boot up
sleep 3

# Start the Python FastAPI Backend in the foreground
echo "Starting Python FastAPI Backend..."
cd /app/backend
uvicorn app.main:app --host 0.0.0.0 --port 8000
