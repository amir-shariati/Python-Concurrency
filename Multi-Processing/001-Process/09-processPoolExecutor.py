import time
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import current_process


def show(name):
    print(f'starting {name}')
    print(f'current_process is {current_process()}')
    time.sleep(3)
    print(f'finishing {name}')


