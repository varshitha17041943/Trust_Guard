# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV VERCEL=1 
# Note: we use VERCEL=1 flag to trigger the /tmp/trustguard.db sqlite routing we set up earlier!

# Install system dependencies and Node.js
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the entire project to the container
COPY . .

# Install MCP Server dependencies (Node.js)
RUN cd mcp && npm install && npm run build

# Install FastAPI Backend dependencies (Python)
RUN cd backend && pip install --no-cache-dir -r requirements.txt

# Make the start script executable
RUN chmod +x /app/start.sh

# Expose the FastAPI port
EXPOSE 8000

# Run the unified start script
CMD ["/app/start.sh"]
