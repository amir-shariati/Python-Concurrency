import time
from multiprocessing import Process, current_process, Queue

numbers = []


def p1_func(queue: Queue):
    print(f'current_process is {current_process()}')
    nums = queue.get()
    nums.extend([1, 2, 3])
    queue.put(nums)
    print(f'p1 nums is: {nums}')


def p2_func(queue: Queue):
    print(f'current_process is {current_process()}')
    nums = queue.get()
    nums.extend([4, 5, 6])
    queue.put(nums)
    print(f'p2 nums is: {nums}')


qs = Queue()
qs.put(numbers)

start = time.perf_counter()

