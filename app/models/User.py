import sqlalchemy
from sqlalchemy.sql.expression import null
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
import bcrypt
from app.db import Base


salt = bcrypt.gensalt()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

    @validates("email")
    def validate_email(self, key, email):
        # only accept if email address contains an "@" sign
        assert "@" in email

        return email

    @validates("password")
    def validate_password(self, key, password):
        assert len(password) > 4

        return bcrypt.hashpw(password.encode("utf-8"), salt)
