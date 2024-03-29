from time import sleep, perf_counter
from threading import Thread
import sys


def show(name):
    print(f'start {name}')
    sleep(2)
    print(f'stop {name}')


start_time = perf_counter()

t1 = Thread(target=show, args=('One',), daemon=True)
t2 = Thread(target=show, args=('Two',), daemon=True)

# start the threads
t1.start()
t2.start()

end_time = perf_counter()

print(f'It took {end_time - start_time: 0.2f} second(S)')

sys.exit(0)
