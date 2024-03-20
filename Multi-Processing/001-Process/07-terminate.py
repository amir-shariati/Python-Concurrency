import time
from multiprocessing import Process, current_process


def show(name):
    print(f'starting {name}')
    print(f'current_process is {current_process()}')
    time.sleep(3)
    print(f'finishing {name}')

