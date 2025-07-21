from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from ..db import SessionLocal

router = APIRouter(prefix='/users', tags=['users'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/{user_id}/segments', response_model=schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    segments = crud.get_user_segments(db, user_id)
    return schemas.UserOut(id=user_id, segments=segments)