import requests

class DataManager:
    def __init__(self):
        self.prices = []
        self.sheety_endpoint = "https://api.sheety.co/02222979d6ec07c1fcf5fdf2a8027db0/flightDeals/prices"
        self.response = requests.get(url=self.sheety_endpoint)
        self.data = self.response.json()
        self.prices_list()

    def prices_list(self):
        for prices in self.data["prices"]:
            self.prices.append(prices)