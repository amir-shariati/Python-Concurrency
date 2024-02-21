from time import sleep, perf_counter
from threading import Thread


def show(name):
    print(f'start {name}')
    sleep(2)
    print(f'stop {name}')


start_time = perf_counter()

t1 = Thread(target=show, args=('One',), daemon=True)
t2 = Thread(target=show, args=('Two',), daemon=True)
