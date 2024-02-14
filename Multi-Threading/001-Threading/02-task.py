from time import sleep, perf_counter
from threading import Thread


def task(id):
    print(f'starting the task {id}')
    sleep(3)
    print(f'the task {id} completed')


start_time = perf_counter()

# create and start 10 threads
threads = [Thread(target=task, args=(n,)) for n in range(1, 11)]


# wait for the threads to complete
for t in threads:
    t.join()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')
