import time
from multiprocessing import Process


def show(name):
    print(f'starting {name}')
    time.sleep(3)
    print(f'finishing {name}')


start = time.perf_counter()

p1 = Process(target=show, args=('One',))
p2 = Process(target=show, args=('Two',))

p1.start()
p2.start()

p1.join()
p2.join()
