from sqlalchemy import Column, Integer, BigInteger, String, DateTime, func, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Segment(Base):
    __tablename__ = 'segments'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    users = relationship('User', secondary='user_segments', back_populates='segments')

class User(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    segments = relationship('Segment', secondary='user_segments', back_populates='users')

class UserSegment(Base):
    __tablename__ = 'user_segments'
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    segment_id = Column(Integer, ForeignKey('segments.id', ondelete='CASCADE'), primary_key=True)
    added_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    __table_args__ = (UniqueConstraint('user_id', 'segment_id', name='uq_user_segment'),)