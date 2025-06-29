from typing import Annotated

from fastapi import Depends, Path, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from core.models import db_helper, Item


async def item_by_id(
    item_id: Annotated[
        int,
        Path(..., gt=0, le=1000, description="Must be between 1 and 1000"),
    ],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Item:
    item = await crud.get_item(session=session, item_id=item_id)
    if item is not None:
        return item

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item with id: {item_id} not found!",
    )
