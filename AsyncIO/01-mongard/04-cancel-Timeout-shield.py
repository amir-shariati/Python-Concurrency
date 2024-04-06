import asyncio
import datetime


async def send_msg(msg, delay):
    print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, {asyncio.current_task().get_name()} is started')
    await asyncio.sleep(delay)
    print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, {asyncio.current_task().get_name()} is Done')


async def main():
    t1 = asyncio.create_task(send_msg('hello', 1), name='Task-1')
    t2 = asyncio.create_task(send_msg('hello', 4), name='Task-2')

    try:
        await asyncio.wait_for(t1, 2)
        await asyncio.wait_for(asyncio.shield(t2), 2)

    except asyncio.TimeoutError:
        if not t2.done():
            print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, {t2.get_name()} continue to be done')
            await t2

