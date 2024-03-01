from threading import Thread, Event, current_thread
from time import sleep


def show_first(f: Event, s: Event):
    print(f'first is starting')
    sleep(1)
    f.set()
    s.wait()
    print(f'first is running')


def show_second(f: Event, s: Event):
    print(f'second is starting')
    sleep(2)
    s.set()
    f.wait()
    print(f'second is running')


def main():
    f_event = Event()
    s_event = Event()

    t1 = Thread(target=show_first, args=(f_event, s_event))
    t2 = Thread(target=show_second, args=(f_event, s_event))

    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
