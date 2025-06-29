from typing import Annotated

from fastapi import APIRouter, Path, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from core.models import db_helper
from .dependencies import item_by_id
from .schemas import ItemCreate, Item


router = APIRouter(prefix="/items", tags=["Items"])


@router.get("/{item_id}")
async def get_item(item: Item = Depends(item_by_id)):
    return item


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=ItemCreate,
)
async def create_item(
    item: ItemCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_item(session=session, item_in=item)


@router.get("/")
async def get_items(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_items(session=session)


@router.delete("/{item_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(
    item: Item = Depends(item_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_item(session=session, item=item)
