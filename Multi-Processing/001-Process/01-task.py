from time import perf_counter
from multiprocessing import Process


def task():
    result = 0
    for _ in range(10**8):
        result += 1
    return result


if __name__ == '__main__':
    start = perf_counter()

    p1 = Process(target=task)
    p2 = Process(target=task)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish = perf_counter()
    print(f'It took {finish-start:.2f} second(s) to finish')
