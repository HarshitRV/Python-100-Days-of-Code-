import pandas
from datetime import datetime
import random
import smtplib
import os

MY_EMAIL = os.environ.get("myEmail")
PASSWORD = os.environ.get("password")

now = datetime.now()

data = pandas.read_csv("birthdays.csv")
data_list  = data.to_dict(orient="records")

if int(now.hour) == 19:
    for person in data_list:
        if now.day == person["day"] and now.month == person["month"]:
            name = person["name"]
            birthday_person_email = person["email"]

            with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r") as file:
                contents = file.read()
                to_send = contents.replace("[NAME]", name)
            
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=birthday_person_email,
                    msg=f"Subject:Happy Birthday \n\n{to_send}"
                )
                connection.close()
