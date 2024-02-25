from time import sleep, perf_counter
from threading import Thread, current_thread, enumerate


def show(name):
    print(f'start {name}')
    sleep(2)
    print(f'stop {name}')


start_time = perf_counter()

t1 = Thread(target=show, args=('One',))
t2 = Thread(target=show, args=('Two',))

# start the threads
t1.start()
t2.start()

# wait for the threads to complete
t1.join()
t2.join()
