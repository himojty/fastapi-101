from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, User, Profile, Article


async def create_user(session: AsyncSession, username: str) -> User:
    user = User(username=username)
    session.add(user)
    await session.commit()
    print("user", user)
    return user
