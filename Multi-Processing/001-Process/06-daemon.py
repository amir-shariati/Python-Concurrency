import time
from multiprocessing import Process, current_process
import sys


def show(name):
    print(f'starting {name}')
    print(f'current_process is {current_process()}')
    time.sleep(3)
    print(f'finishing {name}')


start = time.perf_counter()

p1 = Process(target=show, args=('One',))
p2 = Process(target=show, args=('Two',))

# Daemon
p3 = Process(target=show, args=('Three',), daemon=True)
p4 = Process(target=show, args=('Four',), daemon=True)

p1.start()
p2.start()
p3.start()
p4.start()

p1.join()
p2.join()

end = time.perf_counter()

print(f'It took {end - start:.2f} second(s) to finish')

sys.exit()
