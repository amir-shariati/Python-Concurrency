import asyncio
import datetime
import time


async def say_hello(name: str):
    print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, start coroutine {name}')
    await asyncio.sleep(2)
    print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, hello {name}')


async def main():
    t1 = asyncio.create_task(say_hello('One'))
    t2 = asyncio.create_task(say_hello('Two'))

    await t1
    await t2

    print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, main coroutine, done')

start = time.perf_counter()
asyncio.run(say_hello('One'))
asyncio.run(say_hello('Two'))


end = time.perf_counter()

print(f'It took {end - start:.2f} second(s) to finish')
