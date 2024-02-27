from time import sleep, perf_counter
from threading import Thread, Lock


class Calculator:
    def __init__(self):
        self.num = 0
        self.lock = Lock()

    def add(self):
        with self.lock:
            for _ in range(10000):
                self.num += 1

    def sub(self):
        with self.lock:
            for _ in range(10000):
                self.num -= 1
