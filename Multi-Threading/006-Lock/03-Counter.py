from time import sleep, perf_counter
from threading import Thread, Lock


class Counter:
    def __init__(self):
        self.value = 0
        self.lock = Lock()

    def increase(self, by):
        with self.lock:
            current_value = self.value
            current_value += by

            sleep(0.1)

            self.value = current_value
            print(f'counter={self.value}')
