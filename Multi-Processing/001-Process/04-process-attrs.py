import time
from multiprocessing import Process, current_process
import os


def show(name):
    print(f'starting {name}')
    print(f'current_process is {current_process()}')
    print(f'parent proces is {os.getppid()}')
    print(f'process is {os.getpid()}')
    time.sleep(3)
    print(f'finishing {name}')
