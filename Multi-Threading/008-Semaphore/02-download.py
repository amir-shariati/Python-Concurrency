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


def main():
    # URLs to download
    urls = [
        'https://www.ietf.org/rfc/rfc791.txt',
        'https://www.ietf.org/rfc/rfc792.txt',
        'https://www.ietf.org/rfc/rfc793.txt',
        'https://www.ietf.org/rfc/rfc794.txt',
        'https://www.ietf.org/rfc/rfc795.txt',
    ]

    # Create threads for each download
    threads = [Thread(target=download, args=(url,)) for url in urls]

    [thread.start() for thread in threads]

    # Wait for all threads to complete
    [thread.join() for thread in threads]


