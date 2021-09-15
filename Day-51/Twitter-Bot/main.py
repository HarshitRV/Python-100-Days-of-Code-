from selenium import webdriver
from speedtest import Speedtest
from twitter import Twitter
import os

chrome_driver_path = "/Users/harshitkrvishwakarma/Devlopment/chromedriver"
speed = Speedtest(chrome_driver_path)

tweet_post = f'''Here are the results of my internet speed\nPing: {speed.results[0]}ms
Download: {speed.results[1]}mbps
Upload: {speed.results[2]}mbps'''

email = os.environ.get("email")
password = os.environ.get("password")

tweet = Twitter(
    content=tweet_post,
    webdriver_path=chrome_driver_path,
    email=email,
    pass_=password
)