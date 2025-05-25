from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine(
    "sqlite+aiosqlite:///./test.db",
    echo=True
)

SesionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autoflush=False,
)

class Base(DeclarativeBase):
    pass
async def get_db() -> AsyncSession:
    async with SesionLocal() as session:
        yield session