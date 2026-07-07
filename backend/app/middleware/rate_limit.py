from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
import time
from app.config.settings import settings

# Simple in-memory rate limiter for demonstration
IP_REQUESTS = {}

class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        now = time.time()
        
        if client_ip not in IP_REQUESTS:
            IP_REQUESTS[client_ip] = []
            
        # Clean up old requests
        IP_REQUESTS[client_ip] = [req_time for req_time in IP_REQUESTS[client_ip] if now - req_time < 60]
        
        if len(IP_REQUESTS[client_ip]) >= settings.RATE_LIMIT_PER_MINUTE:
            return JSONResponse(status_code=429, content={"error": "Too many requests", "code": "RATE_LIMIT_EXCEEDED"})
            
        IP_REQUESTS[client_ip].append(now)
        return await call_next(request)
