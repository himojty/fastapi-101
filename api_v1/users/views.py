from typing import Annotated

from fastapi import APIRouter, Path, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from core.models import db_helper

from .schemas import User, UserCreate

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me")
async def get_current_user():
    return {"user": "current"}


@router.get("/{user_id}/")
async def get_user(
    user_id: Annotated[
        int, Path(..., gt=0, le=1000, description="Must be between 1 and 1000")
    ],
):
    return {"user": user_id}


@router.get("/{username}/")
async def get_user_by_username(
    username: str,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> User | None:
    user = await crud.get_user_by_username(session=session, username=username)
    return user


@router.post("/", response_model=UserCreate, status_code=status.HTTP_201_CREATED)
async def create_user(
    user: UserCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    try:
        return await crud.create_user(session=session, user_in=user)
    except:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT)
