import asyncio
from asyncio import TimeoutError


async def send_msg(msg, delay):
    print(f'{asyncio.current_task().get_name()} is started')
    await asyncio.sleep(delay)
    print(f'{asyncio.current_task().get_name()} is Done')


async def main():
    t1 = asyncio.create_task(send_msg('hello', 3))
    t2 = asyncio.create_task(send_msg('hello', 8))


    except TimeoutError as e:
        if t1.cancelled():
            print(f'TimeoutError, {t1.get_name()} is canceled')
        elif t2.cancelled():
            print(f'TimeoutError, {t2.get_name()} is canceled')

asyncio.run(main())
