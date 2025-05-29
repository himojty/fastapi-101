from typing import Annotated

from fastapi import APIRouter, Path

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me")
async def get_current_user():
    return {"user": "current"}


@router.get("/{user_id}")
async def get_user(
    user_id: Annotated[
        int, Path(..., gt=0, le=1000, description="Must be between 1 and 1000")
    ],
):
    return {"user": user_id}
