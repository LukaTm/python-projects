
import datetime as dt
import pandas
import random
import smtplib



now = dt.datetime.now()
data = pandas.read_csv('birthdays.csv')
#print(data)

# random_number = str(random.randint(1,3))
# with open(f'letter_templates/letter_{random_number}.txt','r') as letter3:
#     letter3 = letter3.read() 

random_number = str(random.randint(1, 3))
with open(f'letter_templates/letter_{random_number}.txt') as letter2:
    letter3 = letter2.read()

for (index,row) in data.iterrows():
    row_year = row.year
    row_month = row.month
    row_day = row.day
    if now.month == row_month and now.day == row_day:
        x = data[data.day == now.day]
        #name_to_replace = x.name[0]  # !!!!!!!!!!!!!!!!!!!!!!!!!!
        with open(f'letter_templates/letter_{random_number}.txt') as letter5:
            new_letter = letter5.read()
            new_letter = new_letter.replace("[NAME]", x.name[0])
        my_email = 'emailk'
        password = 'password'
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:HAPPY BIRTHDAY\n\n{new_letter}")











#if now.month in data.month and now.day in data.day:
#     print(data.iterrows())
#     print('adasd')

    #letter3.replace("[NAME]",data.)


