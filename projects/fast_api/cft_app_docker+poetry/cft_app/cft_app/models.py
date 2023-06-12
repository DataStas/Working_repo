from sqlalchemy import Boolean, Column, Integer, String

from .database import Base


class UserInDB(Base):
    __tablename__ = "users"

    employee_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, index=True, unique=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    boss = Column(Boolean)

class Salary(Base):
    __tablename__ = "salaries"

    employee_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    current_salary = Column(Integer, index=True)
    new_salary = Column(Integer, index=True)
    raise_date = Column(String, index=True)
    user_name = Column(String, index=True, unique=True)
