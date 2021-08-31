import requests

class DataManager:
    def __init__(self):
        self.prices = []
        self.sheety_endpoint = ""
        self.response = requests.get(url=self.sheety_endpoint)
        self.data = self.response.json()
        self.prices_list()

    def prices_list(self):
        for prices in self.data["prices"]:
            self.prices.append(prices)