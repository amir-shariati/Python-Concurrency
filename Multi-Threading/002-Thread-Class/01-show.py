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


start_time = perf_counter()

t1 = ShowThread('One', 3)
t2 = ShowThread('Two', 3)

t1.start()
t2.start()

t1.join()
t2.join()

end_time = perf_counter()
print(f'it took {end_time - start_time: 0.2f} second(S)')
