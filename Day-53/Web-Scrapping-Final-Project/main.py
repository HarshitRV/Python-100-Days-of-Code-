from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Scrapping data with BeautifulSoup
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(
    "https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55177535009766%2C%22east%22%3A-122.31488264990234%2C%22south%22%3A37.69926912019228%2C%22north%22%3A37.851235694487485%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D",
    headers=header)

soup = BeautifulSoup(response.text, "html.parser")

all_link_elements = soup.select(".list-card-top a")
all_address_elements = soup.select(".list-card-info address")
all_price_elements = soup.select(".list-card-heading")


listing_links = []
for link in all_link_elements:
    href = link.get("href")
    try:
        if "https" not in href:
            listing_links.append(f"https://www.zillow.com{href}")
        else:
            listing_links.append(href)
    except TypeError:
        pass

addresses = [address.get_text() for address in all_address_elements]

prices_str = [price.get_text() for price in all_price_elements if price.get_text() != ""]
prices = []
for price in prices_str:
    if "+" in price:
        prices.append(price.split('+')[0])
    else:
        prices.append(price.split("/")[0])

# Submitting data to Google Form with Selenium
for i in range(1):
    time.sleep(2)
    driver_path = "/Users/harshitkrvishwakarma/Devlopment/chromedriver"
    driver = webdriver.Chrome(executable_path = driver_path)

    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfZA1LupO_ktMQMtDGeHSvr7-PBvzcNIxUZyAp2vxSuR4L63g/viewform?usp=sf_link")

    time.sleep(1)

    address_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(addresses[i])

    time.sleep(1)
    price_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(prices[i])

    time.sleep(1)
    link_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(listing_links[i])

    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()

    time.sleep(3)
    driver.quit()

print("Done 😁.")