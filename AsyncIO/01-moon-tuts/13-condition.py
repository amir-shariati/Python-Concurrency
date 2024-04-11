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


