from sqlalchemy import Column
from sqlalchemy import Column, Integer, ForeignKey

from app.db import Base


class Vote(Base):
    __tablename__ = "votes"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))
