import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import AsyncSessionLocal, engine
from app.models.base import Base
from app.models.user import User
from app.models.scan import Scan
from app.models.cybertip import CyberTip
from app.security.hashing import get_password_hash

async def seed():
    print("Initializing database tables...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        # create pgvector extension if not exists
        await conn.execute("CREATE EXTENSION IF NOT EXISTS vector;")

    async with AsyncSessionLocal() as session:
        print("Seeding Users...")
        admin = User(email="admin@trustguard.ai", hashed_password=get_password_hash("admin123"), role="admin")
        session.add(admin)
        
        print("Seeding CyberTips...")
        tip = CyberTip(title="Phishing Awareness", content="Always check the sender domain in unexpected emails.", category="Phishing")
        session.add(tip)
        
        print("Seeding Mock Scan...")
        scan = Scan(target="https://fake-login.com", scan_type="URL", status="completed", risk_score=95.0, risk_level="Critical", user=admin)
        session.add(scan)
        
        await session.commit()
        print("Database seeded successfully.")

if __name__ == "__main__":
    asyncio.run(seed())
