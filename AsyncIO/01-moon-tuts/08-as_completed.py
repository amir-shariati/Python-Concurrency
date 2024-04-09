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


async def show_status(session: aiohttp.ClientSession, url: str, delay):
    print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, {asyncio.current_task().get_name()} is started')
    await asyncio.sleep(delay)
    async with session.get(url) as res:
        print(
            f'{datetime.datetime.now().time().strftime("%H:%M:%S")},'
            f' {asyncio.current_task().get_name()}, '
            f' delay:{delay}, status for url {url} is:{res.status}')
        return res.status


async def as_completed_client_session():
    async with aiohttp.ClientSession() as session:
        reqs = [show_status(session, url, random.randint(1, 3)) for url in urls]
        [await coro for coro in asyncio.as_completed(reqs)]


async def main():
    start = time.perf_counter()
    print(f'start coroutine as_completed')
    await as_completed_client_session()
    end = time.perf_counter()
    print(f'as_completed_client_session took {end - start:.2f} second(s) to finish')

asyncio.run(main())
