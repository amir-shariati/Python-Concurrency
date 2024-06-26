import asyncio
import datetime
import time
import aiohttp
import random
import functools
from aiodecorators import Semaphore


urls = [
    'https://www.wikipedia.org/',
    'https://en.wikipedia.org/wiki/Python_(programming_language)',
    'https://en.wikipedia.org/wiki/Go_(programming_language)',
    'https://en.wikipedia.org/wiki/Node.js',
    'https://en.wikipedia.org/wiki/Rust_(programming_language)',
]


async def show_status_with_semaphore(session: aiohttp.ClientSession, url: str, delay, sem: asyncio.Semaphore):
    async with sem:
        print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, {asyncio.current_task().get_name()} is started')
        await asyncio.sleep(delay)
        async with session.get(url) as res:
            print(
                f'{datetime.datetime.now().time().strftime("%H:%M:%S")},'
                f' {asyncio.current_task().get_name()}, '
                f' delay:{delay}, status for url {url} is:{res.status}')
            return res.status


async def semaphore_client_session(sem: asyncio.Semaphore):
    async with aiohttp.ClientSession() as session:
        reqs = [show_status_with_semaphore(session, url, random.randint(1, 3), sem) for url in urls]
        await asyncio.gather(*reqs)


async def show_status(session: aiohttp.ClientSession, url: str, delay):
    print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, {asyncio.current_task().get_name()} is started')
    await asyncio.sleep(delay)
    async with session.get(url) as res:
        print(
            f'{datetime.datetime.now().time().strftime("%H:%M:%S")},'
            f' {asyncio.current_task().get_name()}, '
            f' delay:{delay}, status for url {url} is:{res.status}')
        return res.status


async def semaphore_client_session_semaphore_wrap(sem: asyncio.Semaphore):
    async with aiohttp.ClientSession() as session:
        async def sem_task(task):
            async with sem:
                return await task

        reqs = [sem_task(show_status(session, url, random.randint(1, 3))) for url in urls]
        await asyncio.gather(*reqs)


def rate_limited(max_concurrent):

    def decorator(task):
        semaphore = asyncio.Semaphore(max_concurrent)

        @functools.wraps(task)
        async def wrapper(*args, **kwargs):

            async with semaphore:
                return await task(*args, **kwargs)

        return wrapper

    return decorator


class RateLimited:

    def __init__(self, max_concurrent):
        self.max_concurrent = max_concurrent
        self.semaphore = None

    def __call__(self, task):

        @functools.wraps(task)
        async def wrapper(*args, **kwargs):
            if self.semaphore is None:
                self.semaphore = asyncio.Semaphore(self.max_concurrent)

            async with self.semaphore:
                return await task(*args, **kwargs)

        return wrapper


@RateLimited(max_concurrent=2)
async def show_status_with_decorator(session: aiohttp.ClientSession, url: str, delay):
    print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, {asyncio.current_task().get_name()} is started')
    await asyncio.sleep(delay)
    async with session.get(url) as res:
        print(
            f'{datetime.datetime.now().time().strftime("%H:%M:%S")},'
            f' {asyncio.current_task().get_name()}, '
            f' delay:{delay}, status for url {url} is:{res.status}')
        return res.status


async def semaphore_client_session_call_decorated_task():
    async with aiohttp.ClientSession() as session:
        reqs = [show_status_with_decorator(session, url, random.randint(1, 3)) for url in urls]
        await asyncio.gather(*reqs)


async def main():
    sem = asyncio.Semaphore(2)

    start = time.perf_counter()
    print(f'start semaphore_client_session coroutine ')
    await semaphore_client_session(sem)
    end = time.perf_counter()
    print(f'semaphore_client_session took {end - start:.2f} second(s) to finish')

    print('-------------------------------------------------------------')

    start = time.perf_counter()
    print(f'start semaphore_client_session_semaphore_wrap coroutine ')
    await semaphore_client_session_semaphore_wrap(sem)
    end = time.perf_counter()
    print(f'semaphore_client_session_semaphore_wrap took {end - start:.2f} second(s) to finish')

    print('-------------------------------------------------------------')

    start = time.perf_counter()
    print(f'start semaphore_client_session_call_decorated_task coroutine ')
    await semaphore_client_session_call_decorated_task()
    end = time.perf_counter()
    print(f'semaphore_client_session_call_decorated_task took {end - start:.2f} second(s) to finish')

asyncio.run(main())
