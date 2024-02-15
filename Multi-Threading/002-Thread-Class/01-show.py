from time import sleep, perf_counter
from threading import Thread


def show(name, delay):
    print(f'start {name}')
    sleep(delay)
    print(f'stop {name}')


class ShowThread(Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        show(self.name, self.delay)
