import asyncio
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database.session import engine
from app.models.base import Base
# Import all models to ensure metadata is populated
import app.models

async def bootstrap():
    try:
        print("Connecting to Database and bootstrapping tables...")
        async with engine.begin() as conn:
            print("Creating all tables...")
            await conn.run_sync(Base.metadata.create_all)
        print("Database bootstrapped successfully!")
    except Exception as e:
        print(f"Error bootstrapping database: {e}")

if __name__ == "__main__":
    asyncio.run(bootstrap())
