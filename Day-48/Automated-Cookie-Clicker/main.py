from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

timeover = time.time() + 30
timeout = time.time() + 5

chrome_driver_path = "/Users/harshitkrvishwakarma/Devlopment/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")
# Getting ids of all items
items = driver.find_elements_by_css_selector("#store div")
item_names = [item.get_attribute("id") for item in items]

while True:
    cookie.click()

    if time.time() > timeout:
        # Getting cost of all items
        item_prices = driver.find_elements_by_css_selector("#store b")
        items_cost = []
        for item in item_prices:
            try:
                items_cost.append(int(item.text.split("-")[1].replace(",","")))
            except IndexError:
                pass

        # Keeping cost and name of items in a dict
        items_dict = {}
        for i in range(len(item_names)):
            try:
                items_dict[items_cost[i]] = item_names[i]
            except IndexError:
                pass

        #Getting amount of money we have
        money = int(driver.find_element_by_id("money").text.replace(",",""))

        #Making list of affordable items
        affordable_upgrades = {}
        for cost, id in items_dict.items():
            if money > cost:
                affordable_upgrades[cost] = id

        # Buying the most expensive affordable upgrade 
        try:
            max_id = affordable_upgrades[max(affordable_upgrades)]
            driver.find_element_by_id(max_id).click()
        except ValueError:
            pass
        
        timeout = time.time() + 5

    # Ending the loop after a specific time
    if time.time() > timeover:
        print(driver.find_element_by_id("cps").text) 
        break

driver.quit()