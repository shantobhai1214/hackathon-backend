import time

from fastapi import APIRouter

from app.core.config import settings
from app.models.models import PingResponse

router = APIRouter(tags=["base", "health", "ping", "status", "liveness", "readiness"])


@router.get("/ping", response_model=PingResponse, tags=["Health"])
async def ping() -> PingResponse:
    """
    Health check endpoint for readiness/liveness probes.
    """
    now: int = int(time.time())
    uptime: int = now - int(settings.service_start_time)

    return PingResponse(
        status="ok",
        uptime=uptime,
        timestamp=now,
    ).model_dump()


@router.get("/health", tags=["Health"])
async def health() -> dict:
    """
    Lightweight healthcheck endpoint for Docker/K8s.

    Returns:
        dict: A dictionary containing the health status.

    Example:
        >>> await health()
        {'status': 'ok'}
    """
    return {"status": "ok"}
