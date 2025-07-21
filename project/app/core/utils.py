from sqlalchemy.orm import Session
from sqlalchemy import select, func
import random
from typing import List

def random_assign(db: Session, total: int, percent: float) -> List[int]:
    count = int(total * percent / 100)
    if count <= 0:
        return []
    rows = db.scalars(select(func.random(), func.random(), ).select_from(func.generate_series(1, total))).all()
    # Simplify: fetch all user IDs, shuffle
    user_ids = db.scalars(select(func.distinct('users.id')).select_from('users')).all()
    random.shuffle(user_ids)
    return user_ids[:count]