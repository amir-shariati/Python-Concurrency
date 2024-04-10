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


