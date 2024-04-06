import asyncio
from asyncio import CancelledError


async def send_msg(msg, delay):
    await asyncio.sleep(delay)
    print(f'{msg}, Done')


