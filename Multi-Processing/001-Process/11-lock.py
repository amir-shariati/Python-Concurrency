import time
from multiprocessing import Process, current_process, Lock


def p1_func(num, lock: Lock):
    print(f'current_process is {current_process()}')
    with lock:
        for _ in range(10000):
            num += 1
    print(f'finish process: {current_process()}')


def p2_func(num, lock: Lock):
    print(f'current_process is {current_process()}')
    lock.acquire()
    for _ in range(10000):
        num += 1
    lock.release()
    print(f'finish process: {current_process()}')


lock = Lock()
num = 0

start = time.perf_counter()

p1 = Process(target=p1_func, args=(num, lock))
p2 = Process(target=p2_func, args=(num, lock))

p1.start()
p2.start()

p1.join()
p2.join()

end = time.perf_counter()

print(f'It took {end - start:.2f} second(s) to finish')
