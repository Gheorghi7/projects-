import random
import smtplib
import datetime as dt

email = "valentina161012@gmail.com"
password = "auuyrkvhnioyqlor"

with open('quotes.txt', 'r') as quot:
    arr = quot.readlines()
    rand_arr = random.choice(arr)

if dt.date.today().isoweekday() == 3:
    with smtplib.SMTP("smtp.gmail.com") as smtp:
        smtp.starttls()
        smtp.login(user=email, password=password)
        smtp.sendmail(from_addr=email, to_addrs="gogitacu@gmail.com",
                          msg=f'Subject:Quote of the Day\n\n{rand_arr}')
