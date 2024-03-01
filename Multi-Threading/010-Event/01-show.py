from threading import Thread, Event, current_thread
from time import sleep


def show_first(f: Event, s: Event):
    print(f'first is starting')
    sleep(1)
    f.set()
    s.wait()
    print(f'first is running')

