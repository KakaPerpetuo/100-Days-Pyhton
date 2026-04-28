##################### Extra Hard Starting Project ######################
import pandas as pd
import smtplib
import datetime as dt
import random

# 1. Update the birthdays.csv 
my_email = "[EMAIL_ADDRESS]"
password = "[PASSWORD]"

birthdays_df = pd.read_csv("birthdays.csv")

now = dt.datetime.now()
current_day = now.day   
current_month = now.month

# 2. Check if today matches a birthday in the birthdays.csv

birthdays_match = birthdays_df[
    (birthdays_df["day"] == current_day) & (birthdays_df["month"] == current_month)
]

if not birthdays_match.empty:
    for _, row in birthdays_match.iterrows():
        #print(f"Happy Birthday {row['name']}!")
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        rand_letter = random.choice([1, 2, 3])
        with open(f"letter_templates/letter_{rand_letter}.txt") as letter:
            letter_content = letter.read()
            letter_content = letter_content.replace("[NAME]", row["name"])
            #print(letter_content)

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=row["email"], msg=f"Subject:Happy Birthday!\n\n{letter_content}")




