from fastapi import APIRouter, Depends, HTTPException
from operator import attrgetter
from enum import Enum
from typing import Optional
from app.api.params.sorting import Sort_direction
from app.schemas.skill import Skill

from app.mockup.skills import skills

router = APIRouter()

class Sort_keys(str, Enum):
    score = "score"

@router.get("/", response_model=Skill)
async def get_skills(sort_by: Optional[Sort_keys] = None, sort_direction: Optional[Sort_direction] = None):
    if(sort_by):
        reverse = False
        if(sort_direction == Sort_direction.desc):
            reverse = True
        return sorted(skills, key=attrgetter(sort_by), reverse=reverse)
    return skills