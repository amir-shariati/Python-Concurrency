from time import sleep, perf_counter
from concurrent.futures import ThreadPoolExecutor


def show(name):
    print(f'start {name}')
    sleep(2)
    print(f'stop {name}')
