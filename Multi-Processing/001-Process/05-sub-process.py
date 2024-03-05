import time
from multiprocessing import Process, current_process
import os


def show(name, delay):
    print(f'starting {name}')
    print(f'current_process is {current_process()}')
    print(f'parent proces id of {current_process().name} is {os.getppid()}')
    print(f'process id of {current_process().name} is {os.getpid()}')
    time.sleep(delay)
    print(f'finishing {name}')


