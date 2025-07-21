from sqlalchemy.orm import Session
from sqlalchemy import func, select
from .models import Segment, User, UserSegment
from .core.utils import random_assign
from typing import List

# Segment

def create_segment(db: Session, name: str) -> Segment:
    seg = Segment(name=name)
    db.add(seg)
    db.commit()
    db.refresh(seg)
    return seg

def get_segment(db: Session, seg_id: int) -> Segment | None:
    return db.get(Segment, seg_id)

def get_segment_by_name(db: Session, name: str) -> Segment | None:
    return db.scalar(select(Segment).where(Segment.name == name))

def list_segments(db: Session, skip: int, limit: int) -> List[Segment]:
    return db.scalars(select(Segment).offset(skip).limit(limit)).all()

def update_segment(db: Session, seg_id: int, new_name: str) -> Segment | None:
    seg = get_segment(db, seg_id)
    if seg:
        seg.name = new_name
        db.commit()
        db.refresh(seg)
    return seg

def delete_segment(db: Session, seg_id: int) -> bool:
    seg = get_segment(db, seg_id)
    if seg:
        db.delete(seg)
        db.commit()
        return True
    return False

# UserSegments

def ensure_user(db: Session, user_id: int) -> User:
    user = db.get(User, user_id)
    if not user:
        user = User(id=user_id)
        db.add(user)
        db.commit()
        db.refresh(user)
    return user

def assign_users(db: Session, seg_id: int, user_ids: List[int]) -> List[int]:
    seg = get_segment(db, seg_id)
    if not seg:
        return []
    added = []
    for uid in user_ids:
        user = ensure_user(db, uid)
        if seg not in user.segments:
            user.segments.append(seg)
            added.append(uid)
    db.commit()
    return added

def remove_users(db: Session, seg_id: int, user_ids: List[int]) -> None:
    seg = get_segment(db, seg_id)
    if not seg:
        return
    for uid in user_ids:
        user = db.get(User, uid)
        if user and seg in user.segments:
            user.segments.remove(seg)
    db.commit()

def assign_percentage(db: Session, seg_id: int, percentage: float) -> List[int]:
    total = db.scalar(select(func.count(User.id)))
    ids = random_assign(db, total, percentage)
    return assign_users(db, seg_id, ids)

def get_user_segments(db: Session, user_id: int) -> List[Segment]:
    user = ensure_user(db, user_id)
    return user.segments