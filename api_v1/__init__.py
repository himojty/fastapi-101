__all__ = ("router",)
from .articles.views import router as articles_router
from .users.views import router as users_router
from .items.views import router as items_router
from .demo_auth.views import router as demo_auth_router

from fastapi import APIRouter

router = APIRouter()
router.include_router(router=users_router)
router.include_router(router=items_router)
router.include_router(router=articles_router)
router.include_router(router=demo_auth_router)
