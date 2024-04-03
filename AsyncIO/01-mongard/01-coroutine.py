import asyncio
import datetime
import time


async def say_hello(name: str):
    await asyncio.sleep(2)
    print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, hello {name}')

start = time.perf_counter()
end = time.perf_counter()

print(f'It took {end - start:.2f} second(s) to finish')
