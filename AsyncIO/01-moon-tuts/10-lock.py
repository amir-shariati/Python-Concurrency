import asyncio
import datetime
import time

counter = 0


async def increment(lock: asyncio.Lock):
    print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, '
          f'increment, {asyncio.current_task().get_name()} is started')
    global counter
    async with lock:
        temp_counter = counter
        temp_counter += 1
        await asyncio.sleep(0.01)
        counter = temp_counter
        print(
            f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, '
            f'increment, {asyncio.current_task().get_name()}, counter is: {counter}')


async def decrement(lock: asyncio.Lock):
    print(
        f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, '
        f'decrement, {asyncio.current_task().get_name()} is started')
    global counter
    await lock.acquire()
    temp_counter = counter
    temp_counter -= 1
    await asyncio.sleep(0.01)
    counter = temp_counter
    print(
        f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, '
        f'decrement, {asyncio.current_task().get_name()}, counter is: {counter}')
    lock.release()


async def main():
    global counter
    lock = asyncio.Lock()

    start = time.perf_counter()
    print(f'start increment coroutine by gather')
    tasks = [asyncio.create_task(increment(lock)) for _ in range(6)]
    await asyncio.gather(*tasks)
    end = time.perf_counter()
    print(f'global counter is {counter}')
    print(f'gather_client_session took {end - start:.2f} second(s) to finish')

    print('-------------------------------------------------------------')

    start = time.perf_counter()
    print(f'start decrement coroutine by gather')
    tasks = [asyncio.create_task(decrement(lock)) for _ in range(5)]
    await asyncio.gather(*tasks)
    end = time.perf_counter()
    print(f'global counter is {counter}')
    print(f'gather_client_session took {end - start:.2f} second(s) to finish')

asyncio.run(main())
