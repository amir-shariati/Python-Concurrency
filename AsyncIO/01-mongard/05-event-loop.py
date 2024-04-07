import asyncio
import datetime

async def send_msg(msg, delay):
    print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, {asyncio.current_task().get_name()} is started')
    await asyncio.sleep(delay)
    print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, {asyncio.current_task().get_name()} is Done')


async def main():
    t1 = asyncio.create_task(send_msg('hello', 1), name='Task-1')
    t2 = asyncio.create_task(send_msg('hello', 4), name='Task-2')

    await t1
    await t2

loop = asyncio.new_event_loop()

