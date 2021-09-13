from selenium import webdriver

chrome_driver_path = "/Users/harshitkrvishwakarma/Devlopment/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

dates = driver.find_elements_by_css_selector(".event-widget time")
events = driver.find_elements_by_css_selector(".event-widget li a")

date_list = [date.text for date in dates]
event_list = [event.text for event in events]

event_date_name = {}
for i in range(len(date_list)):
    event_date_name = {
        "time": date_list[i],
        "name": event_list[i]
    }


print(event_date_name)

driver.quit()