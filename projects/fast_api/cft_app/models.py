from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class UserInDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, index=True, unique=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    
    items = relationship("Salary", back_populates="owner")


class Salary(Base):
    __tablename__ = "salaries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    current_salary = Column(Integer, index=True)
    new_salary = Column(Integer, index=True)
    raise_date = Column(String, index=True)
    # description = Column(String, index=True)
    owner_name = Column(String, ForeignKey("users.user_name"))

    owner = relationship("User", back_populates="items")