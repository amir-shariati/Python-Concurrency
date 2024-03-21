import time
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import current_process


def show(name):
    print(f'starting {name}')
    print(f'current_process is {current_process()}')
    time.sleep(3)
    print(f'finishing {name}')


start = time.perf_counter()

with ProcessPoolExecutor(max_workers=2) as executor:
    names = ['One', 'Two', 'Three', 'Four']
    executor.map(show, names)

end = time.perf_counter()

print(f'It took {end - start:.2f} second(s) to finish')
