from time import perf_counter
from threading import Thread
import urllib.request
import urllib.error


class HttpRequestThread(Thread):
    def __init__(self, url: str) -> None:
        super().__init__()
        self.url = url
        self.http_status_code = None
        self.reason = None

    def run(self) -> None:
        try:
            response = urllib.request.urlopen(self.url)
            self.http_status_code = response.code
        except urllib.error.HTTPError as e:
            self.http_status_code = e.code
        except urllib.error.URLError as e:
            self.reason = e.reason


def main():
    urls = [
        'https://httpstat.us/200',
        'https://httpstat.us/400'
    ]
