import time
from multiprocessing import Process, current_process


def show(name):
    print(f'starting {name}')
    print(f'current_process is {current_process()}')
    time.sleep(3)
    print(f'finishing {name}')


def showError():
    print(f'start process {current_process()}')
    raise Exception('somthing wrong')


start = time.perf_counter()

p1 = Process(target=show, args=('One',))
p2 = Process(target=show, args=('Two',))
p3 = Process(target=show, args=('Two',))
p4 = Process(target=showError)
