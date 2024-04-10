from fastapi import APIRouter

from .simple import router as simple_router

v1_router = APIRouter()
v1_router.include_router(simple_router, prefix="/simple")
