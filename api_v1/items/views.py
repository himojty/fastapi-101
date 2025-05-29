from typing import Annotated

from fastapi import APIRouter, Path, status

from .schemas import ItemCreate, Item


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
