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


def main():
    counter = Counter()
    # create threads
    t1 = Thread(target=counter.increase, args=(10, ))
    t2 = Thread(target=counter.increase, args=(20, ))

    # start the threads
    t1.start()
    t2.start()

    # wait for the threads to complete
    t1.join()
    t2.join()

    print(f'The final counter is {counter.value}')


if __name__ == '__main__':
    main()
