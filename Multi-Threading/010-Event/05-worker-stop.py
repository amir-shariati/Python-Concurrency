from threading import Thread, Event
from time import sleep


class Worker(Thread):
        super().__init__(*args, **kwargs)
        self.event = event

    def run(self) -> None:
        for i in range(6):
            print(f'Running #{i + 1}')
            sleep(1)
            if self.event.is_set():
                print('The thread was stopped prematurely.')
                break
        else:
            print('The thread was stopped maturely.')


