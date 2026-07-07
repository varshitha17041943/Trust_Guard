from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repo import user_repo
from app.schemas.user import UserCreate, UserLogin
from app.security.hashing import get_password_hash, verify_password
from app.security.jwt import create_access_token, create_refresh_token, decode_token
from app.exceptions.custom import DomainException, UnauthorizedException
from app.models.audit import AuditLog
from datetime import datetime, timedelta

class AuthService:
    @staticmethod
    async def register(db: AsyncSession, user_in: UserCreate):
        existing = await user_repo.get_by_email(db, user_in.email)
        if existing:
            raise DomainException("Email already registered", 400, "EMAIL_EXISTS")
        hashed = get_password_hash(user_in.password)
        user = await user_repo.create(db, {"email": user_in.email, "hashed_password": hashed})
        
        # Audit log
        audit = AuditLog(user_id=user.id, action="register", details="User registered successfully")
        db.add(audit)
        await db.commit()
        return user

    @staticmethod
    async def login(db: AsyncSession, user_in: UserLogin):
        # Capstone Demo Bypass
        if user_in.email == "admin@trustguard.ai" and user_in.password == "admin":
            refresh_token = create_refresh_token({"sub": "admin@trustguard.ai"})
            return {
                "access_token": create_access_token({"sub": "admin@trustguard.ai"}),
                "refresh_token": refresh_token,
                "token_type": "bearer",
                "user": {"id": 1, "email": "admin@trustguard.ai", "role": "admin"}
            }

        user = await user_repo.get_by_email(db, user_in.email)
        if not user:
            raise UnauthorizedException("Incorrect email or password")
            
        # Check lockout
        if user.locked_until and user.locked_until > datetime.utcnow().replace(tzinfo=user.locked_until.tzinfo):
            raise UnauthorizedException("Account is locked. Try again later.")
            
        if not verify_password(user_in.password, user.hashed_password):
            user.failed_login_attempts += 1
            if user.failed_login_attempts >= 5:
                user.locked_until = datetime.utcnow() + timedelta(minutes=15)
            db.add(AuditLog(user_id=user.id, action="login_failed", details="Invalid password attempt"))
            await db.commit()
            raise UnauthorizedException("Incorrect email or password")
            
        # Success
        user.failed_login_attempts = 0
        user.locked_until = None
        refresh_token = create_refresh_token({"sub": user.email})
        user.refresh_token = refresh_token
        
        db.add(AuditLog(user_id=user.id, action="login_success", details="User logged in"))
        await db.commit()
        
        return {
            "access_token": create_access_token({"sub": user.email}),
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "user": {"id": user.id, "email": user.email, "role": user.role}
        }
        
    @staticmethod
    async def refresh(db: AsyncSession, refresh_token: str):
        try:
            payload = decode_token(refresh_token)
            if payload.get("type") != "refresh":
                raise UnauthorizedException("Invalid token type")
            email = payload.get("sub")
        except Exception:
            raise UnauthorizedException("Invalid refresh token")
            
        user = await user_repo.get_by_email(db, email)
        if not user or user.refresh_token != refresh_token:
            raise UnauthorizedException("Invalid refresh token")
            
        new_access = create_access_token({"sub": user.email})
        new_refresh = create_refresh_token({"sub": user.email})
        user.refresh_token = new_refresh
        await db.commit()
        
        return {
            "access_token": new_access,
            "refresh_token": new_refresh,
            "token_type": "bearer"
        }
