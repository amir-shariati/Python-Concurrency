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


def main():
    calculator = Calculator()

    t1 = Thread(target=calculator.add)
    t2 = Thread(target=calculator.sub)

    # start the threads
    t1.start()
    t2.start()

    # wait for the threads to complete
    t1.join()
    t2.join()

    print(f'num after run threads is: {calculator.num}')
    print('Done')
