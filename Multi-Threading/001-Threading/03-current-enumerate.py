from time import sleep, perf_counter
from threading import Thread, current_thread, enumerate


def show(name):
    print(f'start {name}')
    print(f'current thread is: {current_thread()}')
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

end_time = perf_counter()

print(f'It took {end_time - start_time: 0.2f} second(S)')
