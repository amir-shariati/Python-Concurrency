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

