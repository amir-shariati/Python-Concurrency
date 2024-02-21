from time import sleep
from threading import Thread


def show_timer():
    count = 0
    while True:
        count += 1
        sleep(1)
        print(f'Has been waiting for {count} second(s)...')
