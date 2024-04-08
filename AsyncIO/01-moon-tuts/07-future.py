import asyncio
import datetime
import time


async def set_after(fut: asyncio.Future, delay, value):
    print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, {asyncio.current_task().get_name()} is started')
    await asyncio.sleep(delay)
    fut.set_result(value)
    print(
        f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, {asyncio.current_task().get_name()}, set future:{value}')


async def main():
    loop = asyncio.get_running_loop()

    fut = loop.create_future()

    loop.create_task(set_after(fut, 2, 'Hello'))

    start = time.perf_counter()
    print(f'start coroutine gather')
    result = await fut
    end = time.perf_counter()
    print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, {asyncio.current_task().get_name()} future is: {result}')
    print(f'gather_client_session took {end - start:.2f} second(s) to finish')

