import asyncio
import datetime
import time


async def say_hello(name: str):
    await asyncio.sleep(2)
    print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, hello {name}')

