from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "/Users/harshitkrvishwakarma/Devlopment/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
last_name = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")

first_name.send_keys("Harshit")
last_name.send_keys("Vishwakarma")
email.send_keys("vharshitkr@gmail.com")

submit = driver.find_element_by_xpath('/html/body/form/button')
submit.send_keys(Keys.ENTER)

time.sleep(10)
driver.quit()