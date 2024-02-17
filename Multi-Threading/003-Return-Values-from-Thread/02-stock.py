from threading import Thread
from lxml import html
import requests


class Stock(Thread):
    def __init__(self, symbol):
        super().__init__()
        self.symbol = symbol
        self.url = f'https://finance.yahoo.com/quote/{symbol}'
        self.price = None

    def run(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }
        response = requests.get(self.url, headers=headers)
        if response.status_code == 200:
            # parse the HTML
            tree = html.fromstring(response.text)
            # get the price in text
            price_text = tree.xpath(
                '//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[1]/text()')
            if price_text:
                try:
                    self.price = float(price_text[0].replace(',', ''))
                except ValueError:
                    self.price = None

    def __str__(self):
        return f'{self.symbol}\t{self.price}'


def main():
    symbols = ['MSFT', 'GOOGL', 'AAPL', 'META']
