# # SMTP simple mail transport portocol
# import smtplib

# with open("./emailSender/email_info.txt", 'r') as file:
#     lines = file.read().split()
#     my_email = lines[0]
#     my_password = lines[1]

# with smtplib.SMTP('smtp.gmail.com') as connection: # host name
#     # Transpot Layer Security
#     connection.starttls()  # make connection crepted and secure
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="forworkpenguinlolo@gmail.com",
#                         msg='Subject:Hello\n\nHello, this text made automatically'
#                         )