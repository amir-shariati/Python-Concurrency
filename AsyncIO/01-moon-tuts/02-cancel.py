import asyncio
from asyncio import CancelledError


async def send_msg(msg, delay):
    await asyncio.sleep(delay)
    print(f'{asyncio.current_task().get_name()} is Done')


async def main():
    t1 = asyncio.create_task(send_msg('hello', 3))
    t2 = asyncio.create_task(send_msg('hello', 7))

    sec = 0

    while not t1.done():
        print(f'{t1.get_name()} is running')
        await asyncio.sleep(1)
        sec += 1
        if sec == 5:
            t1.cancel()

    while not t2.done():
        print(f'{t2.get_name()} is running')
        await asyncio.sleep(1)
        sec += 1
        if sec == 5:
            t2.cancel()

    try:
        await t1
        await t2

    except CancelledError:
        if t1.cancelled():
            print(f'{t1.get_name()} is canceled')
        elif t2.cancelled():
            print(f'{t2.get_name()} is canceled')

asyncio.run(main())
