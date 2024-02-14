from time import sleep, perf_counter
from threading import Thread


def show(name):
    print(f'start {name}')
    sleep(2)
    print(f'stop {name}')


start_time = perf_counter()

t1 = Thread(show, args=('One',))
t2 = Thread(show, args=('Two',))

# start the threads
t1.start()
t2.start()

end_time = perf_counter()

print(f'It took {end_time - start_time: 0.2f} second(S)')
