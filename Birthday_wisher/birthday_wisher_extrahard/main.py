##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import csv 
import smtplib
import random as rnd
import datetime as dt
import sys
from os import listdir
from os.path import isfile, join
from os import walk


FILENAME = './birthdays.csv'
FIELD_NAMES = ['name', 'email', 'year', 'month', 'day']
LETTERS_DIR = './letter_templates'


def update_csv():
    with open(FILENAME, 'r', newline='') as file:
        
        new_row_info = input('Ввведите имя, почту, год, месяц, день через пробел').split()
        new_row_info_dict = {}
        for name, row_info in zip(FIELD_NAMES, new_row_info):
            new_row_info_dict[name] = row_info
        new_info = []
        # file_info = csv.reader(file)
        file_info = csv.DictReader(file)
        try:
            for row in file_info:
                new_info.append(row)
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(FILENAME, file_info.line_num, e))

    with open(FILENAME, 'w', newline='') as file:
        if new_row_info_dict not in new_info:
            new_info.append(new_row_info)
            writer = csv.DictWriter(file)
            writer.writerows(new_info)
            print('CSV обновлен')
        else:
            print('Такой получатель уже есть')


def check_today():
    today = dt.datetime.now()
    wish_isneeded = []
    with open(FILENAME, 'r', newline='') as file:
        file_info = csv.DictReader(file)
        try:
            for row in file_info:
                if int(row[FIELD_NAMES[-1]]) == today.day and int(row[FIELD_NAMES[-2]]) == today.month:
                    wish_isneeded.append(row)
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(FILENAME, file_info.line_num, e))
    if bool(wish_isneeded) is True:
        return wish_isneeded
    else:
        print("Никого с ДР нету")
        return False


def send_a_massage(wish_isneeded: list):
    # print(listdir('./letter_templates'))
    # onlyfiles = [f for f in listdir('./letter_templates') if isfile(join('./letter_templates', f))]
    # print(onlyfiles)
    for wish_to in wish_isneeded:
        filenames = next(walk(LETTERS_DIR), (None, None, []))[2]  # [] if no file
        letter = rnd.choice(filenames)
        file_path = LETTERS_DIR + "/" + letter
        with open(file_path) as file:
            letter_info = file.read()            
            letter_info = letter_info.replace('[NAME]', wish_to[FIELD_NAMES[0]])
        
        with open("../SmtpTests/emailSender/email_info.txt", 'r') as file:
            lines = file.read().split()
            my_email = lines[0]
            my_password = lines[1]   

        with smtplib.SMTP('smtp.gmail.com') as connection: # host name
            letter_info = letter_info.encode('utf-8')
            # Transpot Layer Security
            connection.starttls()  # make connection crepted and secure
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=wish_to[FIELD_NAMES[1]],
                                msg=f'Subject:smtplib_test\n\n{letter_info}'
                                )
        

# update_csv()        
if check_today() is not False:
    send_a_massage(check_today())



