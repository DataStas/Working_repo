import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from typing import Annotated, Union
from datetime import timedelta
import crud
import models
import schemas
import auth

models.Base.metadata.create_all(bind=engine)
ACCESS_TOKEN_EXPIRE_MINUTES = 15
from metadata import *


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


@app.post("/token",
          response_model=schemas.Token,
          tags=['token'])
async def login_for_access_token(
    form_data: Annotated[auth.OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
):
    user = auth.authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.user_name}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/users/register_me",
          response_model=Union[schemas.UserInDB, str],
          tags=['register_me'])
async def read_users_me(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    created_user = crud.create_user(db, user=user)
    if type(created_user) != str:
        return "User created"
    else:
        return created_user        


@app.get("/users/me/",
         response_model=schemas.UserInDB,
         tags=['me'])
async def read_users_me(
    current_user: Annotated[schemas.User,
                            Depends(auth.get_current_active_user)],
    db: Session = Depends(get_db)
):
    return crud.get_user_by_name(db, current_user.user_name)


@app.get("/users/me/salary/",
         response_model=Union[schemas.Salary, str],
         tags=['salary'])
async def read_own_salary(
    current_user: Annotated[schemas.User,
                            Depends(auth.get_current_active_user)],
    db: Session = Depends(get_db)
):
    salary = crud.get_salary_by_name(db, current_user.user_name)
    if not salary:
        return "We don't have any information about your salary"
    else:
        return salary

@app.post("/users/set_salary/",
          response_model=schemas.Salary,
         tags=['set_salary'])
def create_salary_plan(
    current_user: Annotated[schemas.User,
                            Depends(auth.get_current_super_user)],
    employee_id: int,
    salary: schemas.SalaryCreate,
    db: Session = Depends(get_db),
):
    return crud.create_user_Salary(db=db, salary=salary, employee_id=employee_id)

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)