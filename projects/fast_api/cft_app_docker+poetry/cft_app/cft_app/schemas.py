from pydantic import BaseModel


class SalaryBase(BaseModel):
    name: str
    surname: str
    user_name: str
    current_salary: int
    new_salary: int | None = None
    raise_date: str | None = None 
    # description: str | None = None


class SalaryCreate(SalaryBase):
    pass


class Salary(SalaryBase):
    employee_id: int
    

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    user_name: str
    password: str


class UserCreate(UserBase):
    pass


class UserInDB(UserCreate):
    email: str
    employee_id: int
    is_active: bool
    boss: bool

    class Config:
        orm_mode = True 


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    user_name: str
    email: str | None = None
    password: str | None = None
    is_active: bool | None = None
    is_boss: bool | None = None