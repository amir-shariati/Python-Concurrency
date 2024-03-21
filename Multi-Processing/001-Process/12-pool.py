import time
from multiprocessing import Pool, current_process, cpu_count


def show(name):
    print(f'{name}, current_process is {current_process()}')
    time.sleep(2)
    print(f'{name}, finish process: {current_process()}')

