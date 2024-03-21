import time
from multiprocessing import Pool, current_process, cpu_count


def show(name):
    print(f'{name}, current_process is {current_process()}')
    time.sleep(2)
    print(f'{name}, finish process: {current_process()}')


names = ['One', 'Two', 'Three', 'Four']

print(f'cpu count is: {cpu_count()}')

start = time.perf_counter()

pool = Pool(processes=2)
pool.map(show, names)