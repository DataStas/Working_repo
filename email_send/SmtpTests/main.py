# # SMTP simple mail transport portocol
import smtplib
import datetime as dt
import random as rnd
import codecs  # когда есть проблема с чтением




# now = dt.datetime.now()
# year = now.year
# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year=1998, month=4, day=10, hour=5)
# print(date_of_birth)

with codecs.open( "BirthdayWisherDay/quotes.txt", "r", "utf_8_sig") as file:
    lines = file.readlines()
    line = rnd.choice(lines)

day_week = dt.datetime.now().day

if day_week == 2: 
    print(line)
    
    with open("BirthdayWisherDay/emailSender/email_info.txt", 'r') as file:
        lines = file.read().split()
        my_email = lines[0]
        my_password = lines[1]

    with smtplib.SMTP('smtp.gmail.com') as connection: # host name
        line = line.encode('utf-8')
        # Transpot Layer Security
        connection.starttls()  # make connection crepted and secure
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="forworkpenguinlolo@gmail.com",
                            msg=f'Subject:smtplib_test\n\n{line}'
                            )