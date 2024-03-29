from time import sleep, perf_counter
from concurrent.futures import ThreadPoolExecutor


def show(name):
    print(f'start {name}')
    sleep(2)
    print(f'stop {name}')


start_time = perf_counter()


with ThreadPoolExecutor(max_workers=2) as executor:
    names = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
    executor.map(show, names)

end_time = perf_counter()

print(f'It took {end_time - start_time: 0.2f} second(S)')