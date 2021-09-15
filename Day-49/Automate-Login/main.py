from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path =  "/Users/harshitkrvishwakarma/Devlopment/chromedriver"
driver = webdriver.Chrome(executable_path = path)

driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

email = driver.find_element_by_id("username")
email.send_keys("email@yourname.com")

password = driver.find_element_by_id("password")
password.send_keys("password_here")

login = driver.find_element_by_class_name("btn__primary--large")
login.click()

time.sleep(10)
driver.quit()