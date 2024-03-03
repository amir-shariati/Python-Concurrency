from time import perf_counter
from multiprocessing import Process


def task(id):
    print(f'task {id} is running')
    result = 0
    for _ in range(10**8):
        result += 1
    print(f'task {id} Done')
    return result


if __name__ == '__main__':
    start = perf_counter()

    p1 = Process(target=task, args=(1,))
    p2 = Process(target=task, args=(2, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish = perf_counter()
    print(f'It took {finish-start:.2f} second(s) to finish')
