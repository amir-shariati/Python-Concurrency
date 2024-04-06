import asyncio
from asyncio import CancelledError


async def send_msg(msg, delay):
    await asyncio.sleep(delay)
    print(f'{msg}, Done')


async def main():
    t1 = asyncio.create_task(send_msg('hello', 3))

    sec = 0

    while not t1.done():
        print(f'{t1.get_name()} is running')
        await asyncio.sleep(1)
        sec += 1
        if sec == 5:
            t1.cancel()

    try:
        await t1

    except CancelledError:
        print(f'{t1.get_name()} is canceled')

asyncio.run(main())
