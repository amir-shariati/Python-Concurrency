import time
from multiprocessing import Process, current_process, Lock


def p1_func(num, lock: Lock):
    print(f'current_process is {current_process()}')
    with lock:
        for _ in range(10000):
            num += 1
    print(f'finish process: {current_process()}')


