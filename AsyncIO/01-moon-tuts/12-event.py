import asyncio
import datetime
import time
import random
import functools


def trigger(event: asyncio.Event):
    event.set()


async def waiter(event: asyncio.Event, delay):
    print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, {asyncio.current_task().get_name()} is started')
    await event.wait()
    print(
        f'{datetime.datetime.now().time().strftime("%H:%M:%S")},'
        f' {asyncio.current_task().get_name()}, '
        f' delay:{delay}, run processing')
    await asyncio.sleep(delay)
    print(
        f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, {asyncio.current_task().get_name()}, finish processing')


async def main():
    event = asyncio.Event()

    start = time.perf_counter()
    print(f'start increment coroutine by gather')
    tasks = [asyncio.create_task(waiter(event, random.randint(1, 3))) for _ in range(3)]
    await asyncio.gather(*tasks)
    end = time.perf_counter()
    print(f'gather_client_session took {end - start:.2f} second(s) to finish')

asyncio.run(main())
