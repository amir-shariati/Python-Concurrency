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



