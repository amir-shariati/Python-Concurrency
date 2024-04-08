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

