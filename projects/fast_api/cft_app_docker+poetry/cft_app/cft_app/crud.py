from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext

from .models import UserInDB, Salary
from .schemas import UserCreate, SalaryCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# def get_user(db: Session, user_id: int):
#     return db.query(models.UserInDB).filter(models.UserInDB.employee_id == user_id).first()


def get_user_by_name(db: Session, user_name: str):
    return db.query(UserInDB).filter(UserInDB.user_name == user_name).first()


# def get_user_by_password(db: Session, password: str):
#     return db.query(models.UserInDB).filter(models.UserInDB.password == password).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.UserInDB).filter(models.UserInDB.email == email).first()


def create_user(db: Session, user: UserCreate):
    email = user.user_name + "@cft.ru"
    password = pwd_context.hash(user.password)
    try:
        db_user = UserInDB(email=email,
                           user_name=user.user_name,
                           password=password,
                           boss=False,
                           is_active=True)
        db.add(db_user)
        db.commit()
    except IntegrityError:
        return 'User is already created'
    db.refresh(db_user)

    return db_user


def get_salary_by_name(db: Session, user_name: str):
    try:
        salary = db.query(Salary).filter(
            Salary.user_name == user_name).first()
    except:
        print('Your salary info is not ready')
    return salary


def create_user_Salary(db: Session, salary: SalaryCreate, employee_id: str):
    db_item = Salary(**salary.dict(), employee_id=employee_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserInDB).offset(skip).limit(limit).all()


def get_salaries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Salary).offset(skip).limit(limit).all()