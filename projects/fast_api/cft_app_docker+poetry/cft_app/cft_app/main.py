from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from typing import Annotated, Union
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm

from .database import Base, engine, SessionLocal
from .crud import create_user, get_user_by_name
from .crud import get_salary_by_name, create_user_Salary
from .crud import get_users, get_salaries

from .schemas import Token, User, UserInDB, Salary, SalaryCreate
from .schemas import UserCreate

from .auth import create_access_token, get_current_super_user
from .auth import authenticate_user, get_current_active_user

from .metadata import tags_metadata, main_description

Base.metadata.create_all(bind=engine)
ACCESS_TOKEN_EXPIRE_MINUTES = 15



app = FastAPI(
    title="СервисЗарплата",
    description=main_description,
    version="0.0.1",
    contact={
        "name": "Станислав Сизов",
        "url": "https://gitlab.com/DataStas",
        "email": "sizovstanislav10@gmail.com",
    },
    openapi_tags=tags_metadata
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", tags=['start'])
def read_root():
    return {"Go to /docs": "Please"}


@app.post("/token",
          response_model=Token,
          tags=['token'])
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.user_name}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/users/register_me",
          response_model=Union[UserInDB, str],
          tags=['register_me'])
async def register_me(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    created_user = create_user(db, user=user)
    if type(created_user) != str:
        return "User created"
    else:
        return created_user


@app.get("/users/me/",
         response_model=UserInDB,
         tags=['me'])
async def read_users_me(
    current_user: Annotated[User,
                            Depends(get_current_active_user)],
    db: Session = Depends(get_db)
):
    return get_user_by_name(db, current_user.user_name)


@app.get("/users/me/salary/",
         response_model=Union[Salary, str],
         tags=['salary'])
async def read_own_salary(
    current_user: Annotated[User,
                            Depends(get_current_active_user)],
    db: Session = Depends(get_db)
):
    salary = get_salary_by_name(db, current_user.user_name)
    if not salary:
        return "We don't have any information about your salary"
    else:
        return salary


@app.post("/users/set_salary/",
          response_model=Salary,
         tags=['set_salary'])
async def create_salary_plan(
    current_user: Annotated[User,
                            Depends(get_current_super_user)],
    employee_id: int,
    salary: SalaryCreate,
    db: Session = Depends(get_db),
):
    return create_user_Salary(db=db,
                              salary=salary,
                              employee_id=employee_id)
    

@app.post("/users/read/",
          response_model=list[UserInDB],
          tags=['read_users'])
async def read_users(
    current_user: Annotated[User,
                            Depends(get_current_super_user)],
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    users = get_users(db, skip=skip, limit=limit)
    return users


@app.post("/users/salaries/read/",
          response_model=list[Salary],
          tags=['read_salaries'])
async def read_salaries(
    current_user: Annotated[User,
                            Depends(get_current_super_user)],
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    salaries = get_salaries(db, skip=skip, limit=limit)
    return salaries
