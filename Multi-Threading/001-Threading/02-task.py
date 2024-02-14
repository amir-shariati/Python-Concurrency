from time import sleep, perf_counter
from threading import Thread


def task(id):
    print(f'starting the task {id}')
    sleep(1)
    print(f'the task {id} completed')


start_time = perf_counter()

# create and start 10 threads
threads = []
for n in range(1, 11):
    t = Thread(target=task, args=(n,))
    threads.append(t)
    t.start()

