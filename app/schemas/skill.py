from pydantic import BaseModel


class Skill(BaseModel):
    title: str
    score: float

    class Config:
        schema_extra = {
            "example": {
                "title": "Beispiele schreiben",
                "score": 1,
            }
        }
