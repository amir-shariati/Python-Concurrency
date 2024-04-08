import asyncio
import datetime
import time
import aiohttp

urls = [

    'https://www.wikipedia.org/',
    'https://en.wikipedia.org/wiki/Python_(programming_language)',
    'https://en.wikipedia.org/wiki/Go_(programming_language)',
    'https://en.wikipedia.org/wiki/Node.js',
    'https://en.wikipedia.org/wiki/Rust_(programming_language)',
]


async def show_status(session: aiohttp.ClientSession, url: str):
    print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, {asyncio.current_task().get_name()} is started')
    async with session.get(url) as res:
        print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, {asyncio.current_task().get_name()}, status:{res.status}')
        return res.status


async def block_client_session():
    async with aiohttp.ClientSession() as session:
        reqs = [await show_status(session, url) for url in urls]
        print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, {asyncio.current_task().get_name()}, reps:{reqs}')


async def gather_client_session():
    async with aiohttp.ClientSession() as session:
        reqs = [show_status(session, url) for url in urls]
        reps = await asyncio.gather(*reqs, return_exceptions=True)
        print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, {asyncio.current_task().get_name()}, reps:{reps}')
        return reps


async def main():

    b1 = asyncio.create_task(block_client_session(), name='Block-1')

    start = time.perf_counter()
    print(f'start coroutine {b1.get_name()}')
    await b1
    end = time.perf_counter()
    print(f'block_client_session took {end - start:.2f} second(s) to finish')

    print('-------------------------------------------------------------------------')

    start = time.perf_counter()
    print(f'start coroutine gather')
    await gather_client_session()
    end = time.perf_counter()
    print(f'gather_client_session took {end - start:.2f} second(s) to finish')


asyncio.run(main())
