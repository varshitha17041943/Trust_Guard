from fastapi import APIRouter, Depends, Response, Cookie
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.services.auth_service import AuthService
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user: dict

@router.post("/register", response_model=UserResponse)
async def register(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    return await AuthService.register(db, user_in)

@router.post("/login", response_model=LoginResponse)
async def login(user_in: UserLogin, response: Response, db: AsyncSession = Depends(get_db)):
    result = await AuthService.login(db, user_in)
    # Set HttpOnly cookie for refresh token
    response.set_cookie(
        key="refresh_token",
        value=result["refresh_token"],
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=7 * 24 * 60 * 60
    )
    return {"access_token": result["access_token"], "token_type": result["token_type"], "user": result["user"]}

@router.post("/refresh")
async def refresh(response: Response, refresh_token: Optional[str] = Cookie(None), db: AsyncSession = Depends(get_db)):
    if not refresh_token:
        from app.exceptions.custom import UnauthorizedException
        raise UnauthorizedException("No refresh token found")
    result = await AuthService.refresh(db, refresh_token)
    response.set_cookie(
        key="refresh_token",
        value=result["refresh_token"],
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=7 * 24 * 60 * 60
    )
    return {"access_token": result["access_token"], "token_type": result["token_type"]}

@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie("refresh_token")
    return {"status": "success"}

@router.get("/profile")
async def profile():
    return {"id": 1, "email": "admin@trustguard.ai", "role": "admin"}
