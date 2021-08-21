import requests
import json

class Quotes:
    def __init__(self):
        self.quote = self.get_quote()

    def get_quote(self):
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " -" + json_data[0]['a']
        return (quote)