from time import sleep, perf_counter
from threading import Thread


def task(id):
    print(f'starting the task {id}')
    sleep(1)
    print(f'the task {id} completed')
