from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models import User, Profile, Article


async def create_user(session: AsyncSession, username: str) -> User:
    user = User(username=username)
    session.add(user)
    await session.commit()
    return user


async def get_user_by_username(session: AsyncSession, username: str) -> User | None:
    stmt = select(User).where(User.username == username)
    user = await session.scalar(stmt)
    return user


async def create_user_profile(
    session: AsyncSession,
    user_id: int,
    first_name: str | None,
    last_name: str | None,
    bio: str | None = None,
) -> Profile:
    profile = Profile(
        user_id=user_id, first_name=first_name, last_name=last_name, bio=bio
    )
    session.add(profile)
    await session.commit()
    return profile


async def show_users_with_profiles(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    users = await session.scalars(stmt)
    for user in users:
        print(user)