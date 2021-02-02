from fastapi import APIRouter

from app.api.endpoints import details, experience, skill

api_router = APIRouter()

api_router.include_router(
    details.router,
    prefix="/details",
    tags=["details"]
)

api_router.include_router(
    experience.router,
    prefix="/experience",
    tags=["experience"]
)

api_router.include_router(
    skill.router,
    prefix="/skill",
    tags=["skill"]
)


@api_router.get("/")
async def root():
    return {"message": "⚡ Welcome ⚡"}
