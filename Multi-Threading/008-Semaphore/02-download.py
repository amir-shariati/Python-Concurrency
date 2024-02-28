from threading import Thread, Semaphore
import urllib.request

MAX_CONCURRENT_DOWNLOADS = 2
semaphore = Semaphore(MAX_CONCURRENT_DOWNLOADS)


def download(url):
    with semaphore:
        print(f"Downloading {url}...")

        response = urllib.request.urlopen(url)
        data = response.read()

        print(f"Finished downloading {url}")

        return data


