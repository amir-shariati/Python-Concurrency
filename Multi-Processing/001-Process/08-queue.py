import time
from multiprocessing import Process, current_process, Queue

numbers = []


def p1_func(queue: Queue):
    print(f'current_process is {current_process()}')
    nums = queue.get()
    nums.extend([1, 2, 3])
    queue.put(nums)
    print(f'p1 nums is: {nums}')


