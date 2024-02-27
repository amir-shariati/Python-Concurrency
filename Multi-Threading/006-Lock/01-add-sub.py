from time import sleep, perf_counter
from threading import Thread, Lock

num = 0


def add():
    global num
    for _ in range(10000):
        num += 1


def sub():
    global num
    for _ in range(10000):
        num -= 1


t1 = Thread(target=add)
t2 = Thread(target=sub)
