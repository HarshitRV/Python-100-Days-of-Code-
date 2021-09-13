from bs4 import BeautifulSoup
import smtplib
import os

MY_EMAIL = os.environ.get("myEmail")
PASSWORD = os.environ.get("pass")

#URL of the product you are interested in on Amazon
URL = ""
#Price you want to buy at
BUY_PRICE = 3000

header = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9"
}
r = requests.get(url=URL, headers=header)

soup = BeautifulSoup(r.text, "html.parser")

price = soup.find(name="span", id="priceblock_dealprice")
cost = float(price.get_text().replace("₹","").replace(",","").replace(".00",""))

if cost < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(
            user = MY_EMAIL,
            password = PASSWORD
        )
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="receiver@email.com",
            msg=f"Subject:Price Fall\n\nNew Price: {cost}\n\nProduct Link\n{URL}"
        )
        connection.close()