from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.security.jwt import decode_token
from app.exceptions.custom import UnauthorizedException
from fastapi.responses import JSONResponse

class JWTAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        public_paths = ["/api/login", "/api/register", "/api/refresh", "/docs", "/openapi.json", "/health", "/version"]
        
        # Allow preflight requests
        if request.method == "OPTIONS":
            return await call_next(request)
            
        # Skip auth for public paths
        if any(request.url.path.startswith(path) for path in public_paths):
            return await call_next(request)
            
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JSONResponse(status_code=401, content={"error": "Missing or invalid authentication token", "code": "UNAUTHORIZED"})
            
        token = auth_header.split(" ")[1]
        try:
            payload = decode_token(token)
            request.state.user = payload
        except UnauthorizedException as e:
            return JSONResponse(status_code=401, content={"error": str(e.message), "code": e.code})
            
        return await call_next(request)
