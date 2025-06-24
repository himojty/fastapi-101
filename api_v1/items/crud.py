from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Item


async def get_items(session: AsyncSession) -> list[Item] | None:
    stmt = select(Item).order_by(Item.id)
    result = await session.execute(stmt)
    items = result.scalars().all()
    return list(items)
