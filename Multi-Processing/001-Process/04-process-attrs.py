import time
from multiprocessing import Process, current_process
import os


def show(name):
    print(f'starting {name}')
    print(f'current_process is {current_process()}')
    print(f'parent proces is {os.getppid()}')
    print(f'process is {os.getpid()}')
    time.sleep(3)
    print(f'finishing {name}')


start = time.perf_counter()

p1 = Process(target=show, args=('One',))
p2 = Process(target=show, args=('Two',))

p1.start()
p2.start()

p1.join()
p2.join()

end = time.perf_counter()

print(f'It took {end - start:.2f} second(s) to finish')