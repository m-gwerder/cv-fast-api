from fastapi import APIRouter
from app.mockup.experiences import experiences

router = APIRouter()

@router.get("/")
async def get_experiences():
    return experiences
