from threading import Thread, Semaphore
import urllib.request

MAX_CONCURRENT_DOWNLOADS = 2
semaphore = Semaphore(MAX_CONCURRENT_DOWNLOADS)


