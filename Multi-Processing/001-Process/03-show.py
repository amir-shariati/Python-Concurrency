import time
from multiprocessing import Process


def show(name):
    print(f'starting {name}')
    time.sleep(3)
    print(f'finishing {name}')
