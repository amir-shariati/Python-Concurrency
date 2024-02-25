from time import sleep, perf_counter
from threading import Thread, current_thread, enumerate


def show(name):
    print(f'start {name}')
    print(f'current thread is: {current_thread()}')
    sleep(2)
    print(f'stop {name}')


start_time = perf_counter()

print(f'log Threads before create any threads: {enumerate()}')

t1 = Thread(target=show, args=('One',))
t2 = Thread(target=show, args=('Two',))

print(f'log Threads after create threads: {enumerate()}')

print(f't1 before start is: {t1}')
print(f't2 before start is: {t2}')

# start the threads
t1.start()
t2.start()

print(f'log Threads after start threads: {enumerate()}')

print(f't1 after start is: {t1}')
print(f't2 after start is: {t2}')

# wait for the threads to complete
t1.join()
t2.join()

print(f't1 after join is: {t1}')
print(f't2 after join is: {t2}')

end_time = perf_counter()

print(f'It took {end_time - start_time: 0.2f} second(S)')
