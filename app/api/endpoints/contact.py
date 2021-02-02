# Not yet working!

from fastapi import APIRouter, Form, Depends
from sqlalchemy.orm import Session
from app import schemas, crud, dependencies
from app.schemas.message import MessageCreate

router = APIRouter()

@router.post("/message/")
async def post_message(message: str = Form(...), db: Session = Depends(dependencies.get_db)):
    message_in = MessageCreate(message = message)
    message_created = crud.message.create(db=db, obj_in=message_in)
    return {"message": "Message succesfully sent", "message_sent": message_created}