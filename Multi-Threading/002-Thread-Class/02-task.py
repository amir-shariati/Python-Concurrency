from time import sleep, perf_counter
from threading import Thread


def task(id):
    print(f'starting the task {id} \n')
    sleep(3)
    print(f'the task {id} completed \n')


class TaskThread(Thread):
    def __init__(self, task_id):
        super().__init__()
        self.task_id = task_id

    def run(self):
        task(self.task_id)