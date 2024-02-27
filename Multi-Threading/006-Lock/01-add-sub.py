from time import sleep, perf_counter
from threading import Thread, Lock

num = 0


def add():
    global num
    for _ in range(10000):
        num += 1
