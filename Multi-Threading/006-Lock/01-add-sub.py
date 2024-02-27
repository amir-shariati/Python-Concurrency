from time import sleep, perf_counter
from threading import Thread, Lock

num = 0
lock = Lock()


def add():
    global num
    with lock:
        for _ in range(10000):
            num += 1


def sub():
    global num
    for _ in range(10000):
        num -= 1


t1 = Thread(target=add)
t2 = Thread(target=sub)

# start the threads
t1.start()
t2.start()

# wait for the threads to complete
t1.join()
t2.join()

print(f'num after run threads is: {num}')
print('Done')
