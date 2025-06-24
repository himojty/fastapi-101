from typing import Annotated

from fastapi import APIRouter, Path, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from .schemas import ItemCreate, Item
from . import crud

router = APIRouter(prefix="/items", tags=["Items"])


@router.get("/{item_id}")
async def get_item(
    item_id: Annotated[
        int,
        Path(..., gt=0, le=1000, description="Must be between 1 and 1000"),
    ],
    q: str | None = None,
):
    return {"item_id": item_id, "q": q}


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=ItemCreate,
)
async def create_item(item: ItemCreate):
    return item


@router.get("/")
async def get_items(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_items(session=session)
