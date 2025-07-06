from fastapi import APIRouter

from app.api.v1.endpoints import (
    base_router,
)

router = APIRouter()

# Include all routers
router.include_router(base_router)
