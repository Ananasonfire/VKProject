from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from ..db import SessionLocal

router = APIRouter(prefix='/segments', tags=['segments'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('', response_model=schemas.SegmentOut, status_code=status.HTTP_201_CREATED)
def create_segment(seg_in: schemas.SegmentCreate, db: Session = Depends(get_db)):
    if crud.get_segment_by_name(db, seg_in.name):
        raise HTTPException(status.HTTP_409_CONFLICT, detail='Segment already exists')
    return crud.create_segment(db, seg_in.name)

@router.get('', response_model=List[schemas.SegmentOut])
def read_segments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.list_segments(db, skip, limit)

@router.put('/{segment_id}', response_model=schemas.SegmentOut)
def update_segment(segment_id: int, seg_upd: schemas.SegmentUpdate, db: Session = Depends(get_db)):
    seg = crud.update_segment(db, segment_id, seg_upd.name)
    if not seg:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Segment not found')
    return seg

@router.delete('/{segment_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_segment(segment_id: int, db: Session = Depends(get_db)):
    if not crud.delete_segment(db, segment_id):
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Segment not found')

@router.post('/{segment_id}/users', response_model=List[int])
def add_users(segment_id: int, body: schemas.AssignUsers, db: Session = Depends(get_db)):
    return crud.assign_users(db, segment_id, body.user_ids)

@router.delete('/{segment_id}/users', status_code=status.HTTP_204_NO_CONTENT)
def delete_users(segment_id: int, body: schemas.AssignUsers, db: Session = Depends(get_db)):
    crud.remove_users(db, segment_id, body.user_ids)

@router.post('/{segment_id}/assign', response_model=List[int])
def assign_percent(segment_id: int, body: schemas.AssignPercent, db: Session = Depends(get_db)):
    return crud.assign_percentage(db, segment_id, body.percentage)