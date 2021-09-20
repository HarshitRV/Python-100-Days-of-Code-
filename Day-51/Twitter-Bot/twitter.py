from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twitter:
    def __init__(self,content, webdriver_path, email, pass_):
        '''Takes four required parameter content:type(str)
        webdriver_path:type(str),email:type(str),pass_type(str)'''
        self.tweet = content
        self.webdriver_path = webdriver_path
        self.email = email
        self.password = pass_
        self.driver = webdriver.Chrome(executable_path = self.webdriver_path)
        self.driver.get("https://twitter.com/login")
        self.login_google()
    
    def login_google(self):
        time.sleep(5)
        try:
            self.driver.find_element_by_name("session[username_or_email]").send_keys(self.email)
            self.driver.find_element_by_name("session[password]").send_keys(self.password)
            self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span').click()
        except:
            self.driver.find_element_by_name("username").send_keys(self.email)
            time.sleep(2)
            self.driver.find_element_by_name("username").send_keys(Keys.ENTER)
            time.sleep(2)
            self.driver.find_element_by_name("password").send_keys(self.password)
            time.sleep(2)
            self.driver.find_element_by_name("password").send_keys(Keys.ENTER)

        time.sleep(2)
        self.write_tweet()

    def write_tweet(self):
        time.sleep(10)
        post = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        post.send_keys(self.tweet)

        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()

        time.sleep(5)
        self.driver.quit()