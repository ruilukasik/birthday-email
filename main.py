##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import random
import pandas as pd
import datetime as dt
import smtplib

MY_EMAIL = "lukasikrui@gmail.com"
PASSWORD = "yocfdeszoqjyaqnr"

now = dt.datetime.now()
birthdays_df = pd.read_csv("birthdays.csv")
for _, row in birthdays_df.iterrows():
    if row["month"] == now.month and row["day"] == now.day:
        name = row["name"]
        email = row["email"]

        letter_nr = random.randint(1, 3)
        with open(f"letter_templates/letter_{letter_nr}.txt") as file:
            letter = file.read()
            letter = letter.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject: Happy Birthday\n\n{letter}"
            )
