import requests
import os
from datetime import datetime
from twilio.rest import Client
import time

TODAY = datetime.now()

STOCK_NAME = "TSLA"
COMPANY_NAME = "tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

ALPHA_API_KEY = os.environ.get("alphaApiKey")
NEWS_API_KEY = os.environ.get("newsApiKey")

parameters_stocks = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":ALPHA_API_KEY
}
response_stock = requests.get(STOCK_ENDPOINT, params=parameters_stocks)
data_stock = response_stock.json()["Time Series (Daily)"]
response_stock.raise_for_status()
# print(data)

list_of_each_day_info = [value for(key, value) in data_stock.items()]
last_two_days_closing = [float(list_of_each_day_info[i]["4. close"]) for i in range(2)]

percentage_change = round(((last_two_days_closing[0]-last_two_days_closing[1])/last_two_days_closing[1])*100, 2)
if percentage_change >= 5:
    stock_change = f"TESLA 🔺{percentage_change}%"
elif percentage_change <= -5:
    stock_change = f"TESLA 🔻{percentage_change}%"
elif percentage_change > 0:
    stock_change = f"TESLA 🔺{percentage_change}%"
else:
    stock_change = f"TESLA 🔻{percentage_change}%"

parameters_news = {
    "qInTitle":COMPANY_NAME,
    "from":TODAY.date(),
    "sortBy":"publishedAt",
    "language":"en",
    "apiKey":NEWS_API_KEY
}
response_news = requests.get(NEWS_ENDPOINT,params=parameters_news)
response_news.raise_for_status()
data_news = response_news.json()["articles"][:3]

# print(data_news)

news_list = [(news["title"], news["description"]) for news in data_news]

# print(news_list)

for news in news_list:
    time.sleep(20)
    account_sid = os.environ.get("accountSID")
    auth_token = os.environ.get("authToken")
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=f"{stock_change}\n\nHeadline: {news[0]}\n\nBrief: {news[1]}",
            from_= os.environ.get("twilioNum"),
            to = os.environ.get("myNum")
        )
    print(message.status)