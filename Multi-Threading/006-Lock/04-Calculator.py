from time import sleep, perf_counter
from threading import Thread, Lock


class Calculator:
    def __init__(self):
        self.num = 0
        self.lock = Lock()

    def add(self):
        with self.lock:
            for _ in range(10):
                self.num += 1
                print(f'in add func, num is: {self.num}')

    def sub(self):
        with self.lock:
            for _ in range(10):
                self.num -= 1
                print(f'in sub func, num is: {self.num}')

    def __call__(self, *args, **kwargs):
        print(f'call Calculator')
        t1 = Thread(target=self.add)
        t2 = Thread(target=self.sub)

        # start the threads
        t1.start()
        t2.start()

        print(f'threads run are: {enumerate()}')

        # wait for the threads to complete
        t1.join()
        t2.join()

        print(f'num after run threads is: {self.num}')
        print('Done')


def main():
    calculator = Calculator()
    calculator()


if __name__ == '__main__':
    main()
