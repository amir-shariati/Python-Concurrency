from threading import Timer, current_thread


def show():
    print(f'current thread is: {current_thread().getName()}')
    print('Done!')
