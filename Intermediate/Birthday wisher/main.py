import random

import pandas
import smtplib
import datetime as dt

data = pandas.read_csv('birthdays.csv')
email = 'valentina161012@gmail.com'
password = 'ihztphjvdpsxzdvf'
name_test = str(data.values[0][0])
email_test = str(data.values[0][1])

with open(f"letter_templates/letter_{random.randint(1,3)}.txt", 'r') as letter:
    let = letter.read().replace('[NAME]', name_test)

if dt.date.today() == dt.date(year=int(data.values[0][2]), month=int(data.values[0][3]), day=int(data.values[0][4])):
    with smtplib.SMTP('smtp.gmail.com') as smtp:
        smtp.starttls()
        smtp.login(password=password, user=email)
        smtp.sendmail(msg=f"Subject:{name_test}\n\n{let}", from_addr=email, to_addrs=email_test)
        print('Email sendet')
