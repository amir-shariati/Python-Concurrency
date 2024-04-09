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

