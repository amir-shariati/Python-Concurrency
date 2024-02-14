from time import sleep, perf_counter
from threading import Thread


def show(name):
    print(f'start {name}')
    sleep(2)
    print(f'stop {name}')
