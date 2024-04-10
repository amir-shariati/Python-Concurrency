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


