from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Article

from . import crud


async def article_by_id(
    article_id: Annotated[
        int,
        Path(..., gt=0, le=1000, description="Must be between 1 and 1000"),
    ],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Article:
    article = await crud.get_article(session=session, article_id=article_id)
    if article is not None:
        return article

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {article_id} not found!",
    )
