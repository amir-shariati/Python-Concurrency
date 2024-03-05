import time
from multiprocessing import Process, current_process
import os


def show(name, delay):
    print(f'starting {name}')
    print(f'current_process is {current_process()}')
    print(f'parent proces id of {current_process().name} is {os.getppid()}')
    print(f'process id of {current_process().name} is {os.getpid()}')
    time.sleep(delay)
    print(f'finishing {name}')


class ShowProcess(Process):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        show(self.name, self.delay)


start = time.perf_counter()

p1 = ShowProcess(name='One', delay=2)
p2 = ShowProcess(name='Two', delay=3)

p1.start()
p2.start()

p1.join()
p2.join()

end = time.perf_counter()

print(f'It took {end - start:.2f} second(s) to finish')