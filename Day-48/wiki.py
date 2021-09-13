from selenium import webdriver

chrome_driver_path = "/Users/harshitkrvishwakarma/Devlopment/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')

print(article_count.text)

driver.quit()