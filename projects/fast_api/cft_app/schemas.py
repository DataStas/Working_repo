from pydantic import BaseModel


class SalaryBase(BaseModel):
    name: str 
    current_salary: int
    new_salary: int | None = None
    raise_date: str | None = None 
    description: str | None = None


class SalaryCreate(SalaryBase):
    pass


class Salary(SalaryBase):
    id: int
    owner_name: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    user_name: str
    email: str


class UserCreate(UserBase):
    password: str


class UserInDB(UserCreate):
    id: int
    is_active: bool
    salaries: list[Salary] = []

    class Config:
        orm_mode = True 


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None

  
class User(BaseModel):
    username: str
    email: str | None = None
    disabled: bool | None = None