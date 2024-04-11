import asyncio
import datetime
import time
import random


async def trigger(condition: asyncio.Condition):
    print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, {asyncio.current_task().get_name()} is started')
    await asyncio.sleep(5)

    async with condition:
        print('-------------------------------------------------------------')
        print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, {asyncio.current_task().get_name()}, Notify all tasks')
        condition.notify_all()
        print('-------------------------------------------------------------')


async def waiter(condition: asyncio.Condition, delay):
    print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, {asyncio.current_task().get_name()} is started')
    async with condition:
        print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, {asyncio.current_task().get_name()} is locked')
        await condition.wait()
        print(
            f'{datetime.datetime.now().time().strftime("%H:%M:%S")},'
            f' {asyncio.current_task().get_name()}, '
            f' delay:{delay}, run processing')
        await asyncio.sleep(delay)
        print(
            f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, {asyncio.current_task().get_name()}, finish processing')


