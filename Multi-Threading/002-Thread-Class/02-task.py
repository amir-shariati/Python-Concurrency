from time import sleep, perf_counter
from threading import Thread


class TaskThread(Thread):
    def __init__(self, task_id, delay):
        super().__init__()
        self.task_id = task_id
        self.delay = delay

    def run(self):
        self.task(self.task_id, self.delay)

    def task(self, id, delay):
        print(f'starting the task {id} ')
        sleep(3)
        print(f'the task {id} completed ')


start_time = perf_counter()

threads = [TaskThread(n, 3) for n in range(1, 11)]

for t in threads:
    t.start()

for t in threads:
    t.join()

end_time = perf_counter()

print(f'\n It took {end_time- start_time: 0.2f} second(s) to complete.')
