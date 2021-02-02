from pydantic import BaseModel


class MessageBase(BaseModel):
    message: str

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    id: int

    class Config:
        orm_mode = True