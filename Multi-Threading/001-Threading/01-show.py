from time import sleep, perf_counter
from threading import Thread


def show(name):
    print(f'start {name}')
    sleep(2)
    print(f'stop {name}')


start_time = perf_counter()
show('One')
show('Two')
end_time = perf_counter()