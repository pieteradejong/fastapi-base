from fastapi import APIRouter, status
from pydantic import BaseModel
from typing import Literal, Optional
from app.config import logger


class SuccessResponse(BaseModel):
    status: Literal["success"]
    message: str


class HealthResponse(BaseModel):
    status: Literal["success", "error"]
    result: Optional[list]
    message: Optional[str]


router = APIRouter()


@router.get("/", response_model=SuccessResponse, status_code=status.HTTP_200_OK)
async def root():
    logger.info("Received root request")
    return SuccessResponse(
        status="success", message="Template application using FastAPI."
    )


@router.get("/health", response_model=HealthResponse, status_code=status.HTTP_200_OK)
async def health():
    is_healthy = True

    if is_healthy:
        return HealthResponse(
            status="success", result=[], message="Application is healthy."
        )
    else:
        return HealthResponse(
            status="error",
            result=[],
            message="Application is not healthy, there is an issue.",
        )
