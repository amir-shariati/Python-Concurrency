from threading import Thread, Event
from urllib import request


def download_file(url, event):
    # Download the file form URL
    print(f"Downloading file from {url}...")
    filename, _ = request.urlretrieve(url, "rfc793.txt")

    # File download completed, set the event
    event.set()


def process_file(event):
    print("Waiting for the file to be downloaded...")
    event.wait()  # Wait for the event to be set

    # File has been downloaded, start processing it
    print("File download completed. Starting file processing...")

    # Count the number of words in the file
    word_count = 0
    with open("rfc793.txt", "r") as file:
        for line in file:
            words = line.split()
            word_count += len(words)

    # Print the word count
    print(f"Number of words in the file: {word_count}")


