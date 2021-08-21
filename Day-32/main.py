import smtplib
import datetime as dt
from quote_generator import Quotes

my_email = "vharshitkr360@gmail.com"
password = "If(pass==1){access;}else{deny;}"

quotes = Quotes()

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() #encrypts the email and secures the connection
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="vharshitkr360@yahoo.com",
            msg=f"Subject:Monday Motivation\n\n{quotes.quote}"
        )
    connection.close()

