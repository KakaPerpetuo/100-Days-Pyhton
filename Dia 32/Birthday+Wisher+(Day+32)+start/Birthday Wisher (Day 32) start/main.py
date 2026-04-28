import smtplib
import datetime as dt
import random

my_email = "[EMAIL_ADDRESS]"
password = "[PASSWORD]"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email, 
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )

#now = dt.datetime.now()
#year = now.year
#month = now.month
#day_of_week = now.weekday()
#print(day_of_week)

#date_of_birth = dt.datetime(year=2001, month=5, day=16)
#print(date_of_birth)
