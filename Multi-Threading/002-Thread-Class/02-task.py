from time import sleep, perf_counter
from threading import Thread


def task(id):
    print(f'starting the task {id} \n')
    sleep(3)
    print(f'the task {id} completed \n')