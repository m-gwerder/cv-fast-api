from pydantic import BaseModel
from typing import Optional
from enum import Enum
from datetime import date


class ExperienceType(str, Enum):
    education = "education"
    work = "work"

class Experience(BaseModel):
    title: str
    institution: str
    city: str
    description: Optional[str] = None
    startDate: date
    endDate: Optional[date]
    experienceType: ExperienceType
