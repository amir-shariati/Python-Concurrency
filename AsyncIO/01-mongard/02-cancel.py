import asyncio
from asyncio import CancelledError


async def send_msg(msg, delay):
    await asyncio.sleep(delay)
    print(f'{msg}, Done')


async def main():
    t1 = asyncio.create_task(send_msg('hello', 3))

    sec = 0

