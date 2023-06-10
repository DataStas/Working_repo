from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class UserInDB(Base):
    __tablename__ = "users"

    employee_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, index=True, unique=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    boss = Column(Boolean)
    
    # items = relationship("Salary", back_populates="owner")
    # token 


class Salary(Base):
    __tablename__ = "salaries"

    employee_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    current_salary = Column(Integer, index=True)
    new_salary = Column(Integer, index=True)
    raise_date = Column(String, index=True)
    user_name = Column(String, index=True, unique=True)
    
    # owner_id = Column(Integer, ForeignKey("users.employee_id"))
    # owner = relationship("UserInDB", back_populates="items")
    # description = Column(String, index=True)
