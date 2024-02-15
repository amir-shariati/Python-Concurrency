from time import sleep, perf_counter
from threading import Thread


def show(name, delay):
    print(f'start {name}')
    sleep(delay)
    print(f'stop {name}')
