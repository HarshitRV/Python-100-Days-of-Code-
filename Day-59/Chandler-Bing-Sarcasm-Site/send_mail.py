import smtplib
import os

class Mail:
    def __init__(self, name, sender_email, phone, message):
        self.email = os.environ.get("email")
        self.pass_ = os.environ.get("pass_")
        self.to_email = os.environ.get("to_email")

        self.name = name
        self.sender_email = sender_email
        self.phone = phone
        self.message = message
    
    def send_mail(self):
        with smtplib.SMTP("smtp.gmail.com") as c:
            c.starttls()
            c.login(user=self.email, password=self.pass_)
            c.sendmail(
                from_addr=self.email,
                to_addrs=self.to_email,
                msg=f"Subject:API Support\n\nName: {self.name}\n \
                      Email: {self.email}\nPhone: {self.phone}\n \
                      Message: {self.message}"
            )
            c.close()
