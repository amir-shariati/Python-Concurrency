from threading import Thread, Event
from time import sleep


def task(event: Event) -> None:
    for i in range(6):
        print(f'Running #{i + 1}')
        sleep(1)
        if event.is_set():
            print('The thread was stopped prematurely.')
            break
    else:
        print('The thread was stopped maturely.')


