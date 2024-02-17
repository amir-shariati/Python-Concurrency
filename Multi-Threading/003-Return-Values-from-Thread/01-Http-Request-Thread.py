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

    start_time = perf_counter()

    threads = [HttpRequestThread(url) for url in urls]

    [t.start() for t in threads]

    [t.join() for t in threads]

    end_time = perf_counter()

    print(f'\n It took {end_time - start_time: 0.2f} second(s) to complete.')

    # display the URLs with HTTP status codes
    [print(f'{t.url}: {t.http_status_code}') for t in threads]
