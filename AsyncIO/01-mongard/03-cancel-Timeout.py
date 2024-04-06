import asyncio
from asyncio import TimeoutError


async def send_msg(msg, delay):
    print(f'{asyncio.current_task().get_name()} is started')
    await asyncio.sleep(delay)
    print(f'{asyncio.current_task().get_name()} is Done')


