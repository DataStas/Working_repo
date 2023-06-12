import sqlite3
import random
from passlib.context import CryptContext

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
CHARS = '+-/*!&$#?=@<>abcdefghijklnopqrst\
uvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

# Подготовка информации для создания пользователей
user_names = ['Petya',
              'Stepa',
              'Tolya',
              'Vadim',
              'Alena',
              'Tanya',
              'Anna']
names = ["Петя",
         "Степа",
         "Толик",
         "Вадим Алексеевич",
         "Алена",
         "Таня",
         "Анна"]
boss = [1 if len(name) > 8 else 0 for name in names]
surnames = ['Иванов',
            'Петров',
            'Сидоров',
            'Николаев',
            'Петрова',
            'Сидорова',
            'Николаева']
email = [name+'@cft.ru' for name in user_names]
salary = [random.randint(100000, 100000) for _ in names]
new_salary = [random.randint(100000, 200000) for _ in names]

# генерация паролей
passwords = []
for _ in range(len(names)):
    s = ''
    for _ in range(10):
        s += random.choice(CHARS)
    passwords.append(s)

# сохранение паролей, чтобы иметь возможность зайти
with open('pass.txt', 'w') as f:
    f.write(str([(pas, name) for pas, name in zip(passwords, user_names)]))

# хэширование паролей
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
hashed_passwords = []
for password in passwords:
    hashed_passwords.append(pwd_context.hash(password))

# создание БД
db = sqlite3.connect("users.db")
cursor = db.cursor()
cursor.execute("CREATE TABLE users (employee_id INTEGER PRIMARY KEY,\
               user_name varchar(250) NOT NULL UNIQUE, \
               email varchar(250) NOT NULL UNIQUE,\
               password varchar(250) NOT NULL,  \
               is_active BOOL NOT NULL, \
               boss BOOL NOT NULL)")
cursor.execute("CREATE TABLE salaries (employee_id INTEGER PRIMARY KEY,\
               name varchar(250) NOT NULL UNIQUE, \
               surname varchar(250) NOT NULL, \
               current_salary INTEGER NOT NULL, \
               new_salary INTEGER NOT NULL, \
               raise_date varchar(250) NOT NULL,\
               user_name varchar(250) NOT NULL UNIQUE)")

# запись подготовленной информации в БД
for ind, name in enumerate(user_names):
    cursor.execute(f"INSERT INTO users VALUES({ind}, '{name}',\
                   '{email[ind]}', \
                   '{hashed_passwords[ind]}', True, \
                   '{boss[ind]}')")
    db.commit()

for ind, name in enumerate(names):
    cursor.execute(f"INSERT INTO salaries VALUES({ind}, '{name}', \
                   '{surnames[ind]}', '{salary[ind]}', \
                   '{new_salary[ind]}', '10/07/23', '{user_names[ind]}')")
    db.commit()