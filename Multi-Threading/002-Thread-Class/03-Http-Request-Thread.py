from time import sleep, perf_counter
from threading import Thread
import urllib.request
import urllib.error


class HttpRequestThread(Thread):
    def __init__(self, url: str) -> None:
        super().__init__()
        self.url = url

    def run(self) -> None:
        print(f'Checking {self.url} ...')
        try:
            response = urllib.request.urlopen(self.url)
            print(response.code)
        except urllib.error.HTTPError as e:
            print(e.code)
        except urllib.error.URLError as e:
            print(e.reason)


def main():
    urls = [
        'https://httpstat.us/200',
        'https://httpstat.us/400'
    ]
