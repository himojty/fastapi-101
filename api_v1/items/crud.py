"""
Create
Read
Update
Delete
"""

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Item
from .schemas import ItemCreate


async def get_items(
    session: AsyncSession,
) -> list[Item] | None:
    stmt = select(Item).order_by(Item.id)
    result = await session.execute(stmt)
    items = result.scalars().all()
    return list(items)


async def get_item(
    session: AsyncSession,
    item_id: int,
) -> Item | None:
    return await session.get(Item, item_id)


async def create_item(
    session: AsyncSession,
    item_in: ItemCreate,
) -> Item:
    item = Item(**item_in.model_dump())
    session.add(item)
    await session.commit()
    return item


async def delete_item(
    session: AsyncSession,
    item: Item,
) -> None:
    await session.delete(item)
    await session.commit()
