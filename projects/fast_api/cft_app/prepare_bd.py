import sqlite3
import random
from werkzeug.security import generate_password_hash


CHARS = '+-/*!&$#?=@<>abcdefghijklnopqrst\
uvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


db = sqlite3.connect("users.db")

cursor = db.cursor()
# создание БД
cursor.execute("CREATE TABLE users (employee_id INTEGER PRIMARY KEY,\
               user_name varchar(250) NOT NULL UNIQUE, \
               email varchar(250) NOT NULL UNIQUE,\
               password varchar(250) NOT NULL,  \
               is_active BOOL NOT NULL)")
cursor.execute("CREATE TABLE salaries (employee_id INTEGER PRIMARY KEY,\
               name varchar(250) NOT NULL UNIQUE, \
               surname varchar(250) NOT NULL, \
               current_salary INTEGER NOT NULL, \
               new_salary INTEGER NOT NULL, \
               raise_date varchar(250) NOT NULL) ")

# Подготовка информации для создания пользователей
user_names = ['Petya',
              'Stepa',
              'Tolya',
              'Vadim']
names = ["Петя",
         "Степа",
         "Толик",
         "Вадим Алексеевич"]
surnames = ['Иванов',
            'Петров',
            'Сидоров',
            'Николаев']
email = [name+'@cft.ru' for name in user_names]
salary = [random.randint(100000, 100000) for _ in names]
new_salary = [random.randint(100000, 200000) for _ in names]
with open('pass.txt', 'w') as f:
    passwords = []
    for _ in range(len(names)):
        s = ''
        for _ in range(10):
            s += random.choice(CHARS)
        passwords.append(s)
    f.write(str(passwords))

hashed_passwords = []
for password in passwords:
    hashed_passwords.append(generate_password_hash(
            password=password,
            method='pbkdf2:sha256',
            salt_length=8
        ))

for ind, name in enumerate(user_names):
    cursor.execute(f"INSERT INTO users VALUES({ind}, '{name}',\
                   '{hashed_passwords[ind]}', \
                   '{email[ind]}', 'expired', '00:00:00')")
    db.commit()

for ind, name in enumerate(names):
    cursor.execute(f"INSERT INTO salary VALUES({ind}, '{name}', \
                   '{surnames[ind]}', '{salary[ind]}', \
                   '{new_salary[ind]}', '10/06/23')")
    db.commit()