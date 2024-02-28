from threading import Thread, Semaphore, current_thread
from time import sleep

lock = Semaphore(value=2)


def show():
    with lock:
        print(f'current thread is: {current_thread().getName()}')
        sleep(2)
