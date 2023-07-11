import smtplib



import datetime as dt
import random


now = dt.datetime.now()
year = now.year
month = now.month
second = now.second
day_of_week = now.weekday() # what day,starts from 0 so 0 - pirmdiena

date_of_birth = dt.datetime(year= 2004, month=7 ,day=1, hour=11 ) # ... have default values

current_day = now.weekday()
if current_day + 1 == 6:
    with open('quotes.txt','r') as quotes:
        random_one_line = random.choice(quotes.readlines())
        my_email = 'email@gmail.com'
        password = 'access_passowrd'
        with smtplib.SMTP("smtp.gmail.com") as connection:
             connection.starttls()
             connection.login(user=my_email, password=password)
             connection.sendmail(
                 from_addr=my_email,
                 to_addrs=my_email,
                 msg=f"Subject:Stop it\n\n{random_one_line}")




