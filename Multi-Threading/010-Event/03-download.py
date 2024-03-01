from threading import Thread, Event
from urllib import request


def download_file(url, event):
    # Download the file form URL
    print(f"Downloading file from {url}...")
    filename, _ = request.urlretrieve(url, "rfc793.txt")

    # File download completed, set the event
    event.set()


