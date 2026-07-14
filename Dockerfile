# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV VERCEL=1 

# Set the working directory in the container
WORKDIR /app

# Copy the entire project to the container
COPY . .

# Install MCP Server dependencies (Python)
RUN cd mcp && pip install --no-cache-dir -r requirements.txt

# Install FastAPI Backend dependencies (Python)
RUN cd backend && pip install --no-cache-dir -r requirements.txt

# Make the start script executable
RUN chmod +x /app/start.sh

# Expose the FastAPI port
EXPOSE 8000

# Run the unified start script
CMD ["/app/start.sh"]
