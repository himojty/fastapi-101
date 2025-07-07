import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from core.models import db_helper, Profile, User


async def create_profile(
    session: AsyncSession,
    user_id: int,
    first_name: str | None = None,
    last_name: str | None = None,
    bio: str | None = None,
) -> Profile:
    profile = Profile(
        first_name=first_name,
        last_name=last_name,
        bio=bio,
        user_id=user_id,
    )
    session.add(profile)
    await session.commit()
    return profile


async def show_users_with_profiles(session: AsyncSession):
    stmt = select(User).options(joinedload(User.profile)).order_by(User.id)
    users = await session.scalars(stmt)
    for user in users:
        print(user)
        print(f" - first_name: {user.profile.first_name}")
        print(f" - last_name: {user.profile.last_name}")
        print(f" - bio: {user.profile.bio}")


async def main():
    async with db_helper.session_factory() as session:
        # await create_profile(
        #     session=session,
        #     user_id=0,
        #     first_name="Nobody",
        # )
        # await create_profile(
        #     session=session,
        #     user_id=7,
        #     last_name="Бобиков",
        #     first_name="Тимоха",
        # )
        # await create_profile(
        #     session=session,
        #     user_id=14,
        #     last_name="Pinkman",
        #     first_name="Jessy",
        # )
        # await create_profile(
        #     session=session,
        #     user_id=13,
        #     bio="Умный человек в очках",
        #     first_name="Ян",
        #     last_name="Топлес",
        # )

        await show_users_with_profiles(session=session)


if __name__ == "__main__":
    asyncio.run(main())
