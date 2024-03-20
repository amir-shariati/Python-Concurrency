import time
from multiprocessing import Process, current_process


def show(name):
    print(f'starting {name}')
    print(f'current_process is {current_process()}')
    time.sleep(3)
    print(f'finishing {name}')


def showError():
    print(f'start process {current_process()}')
    raise Exception('somthing wrong')


start = time.perf_counter()

p1 = Process(target=show, args=('One',))
p2 = Process(target=show, args=('Two',))
p3 = Process(target=show, args=('Two',))
p4 = Process(target=showError)

p1.start()
p2.start()
p3.start()
p4.start()

print(f'{p1.name} is alive: {p1.is_alive()}')
print(f'{p2.name} is alive: {p2.is_alive()}')
print(f'{p3.name} is alive: {p3.is_alive()}')
print(f'{p4.name} is alive: {p4.is_alive()}')

p2.terminate()
p3.kill()

p1.join()
p2.join()
p3.join()
p4.join()

print(f'{p1.name} is alive: {p1.is_alive()}')
print(f'{p2.name} is alive: {p2.is_alive()}')
print(f'{p3.name} is alive: {p3.is_alive()}')
print(f'{p4.name} is alive: {p4.is_alive()}')
