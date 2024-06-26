import asyncio
import datetime
import random
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


async def wait_client_session():
    async with aiohttp.ClientSession() as session:
        reqs = [asyncio.create_task(show_status(session, url, random.randint(1, 3))) for url in urls]
        done, pending = await asyncio.wait(reqs)
        return done, pending


async def wait_first_completed_client_session():
    async with aiohttp.ClientSession() as session:
        reqs = [asyncio.create_task(show_status(session, url, random.randint(1, 3))) for url in urls]
        done, pending = await asyncio.wait(reqs, return_when=asyncio.FIRST_COMPLETED)
        return done, pending


async def wait_first_exception_client_session():
    async with aiohttp.ClientSession() as session:
        reqs = [asyncio.create_task(show_status(session, url, random.randint(1, 3))) for url in urls]
        done, pending = await asyncio.wait(reqs, return_when=asyncio.FIRST_EXCEPTION)
        return done, pending


async def main():
    start = time.perf_counter()
    print(f'start coroutine wait_client_session')
    done, pending = await wait_client_session()
    end = time.perf_counter()
    for done_task in done:
        print(
            f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, '
            f'done task is: {done_task.get_name()}, '
            f'result: {done_task.result()}'
        )
    for pending_task in pending:
        print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, pending is: {pending_task}')
    print(f'wait_client_session took {end - start:.2f} second(s) to finish')

    print('-------------------------------------------------------------')

    start = time.perf_counter()
    print(f'start coroutine wait_first_completed_client_session')
    done, pending = await wait_first_completed_client_session()
    end = time.perf_counter()
    for done_task in done:
        print(
            f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, '
            f'done task is: {done_task.get_name()}, '
            f'result: {done_task.result()}'
        )
    for pending_task in pending:
        print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, pending task is: {pending_task.get_name()}')
    print(f'wait_first_completed_client_session took {end - start:.2f} second(s) to finish')

    print('-------------------------------------------------------------')

    start = time.perf_counter()
    print(f'start coroutine wait_first_exception_client_session')
    done, pending = await wait_first_exception_client_session()
    end = time.perf_counter()
    for done_task in done:
        print(
            f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, '
            f'done task is: {done_task.get_name()}, '
            f'result: {done_task.result()}'
        )
    for pending_task in pending:
        print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, pending task is: {pending_task.get_name()}')
    print(f'wait_first_exception_client_session took {end - start:.2f} second(s) to finish')


asyncio.run(main())
