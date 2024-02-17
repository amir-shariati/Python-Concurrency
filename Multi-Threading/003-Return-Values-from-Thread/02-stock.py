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
        pass
