import asyncio
import datetime
import time


async def main():

    start = time.perf_counter()
    print(f'start create_subprocess_exec coroutine')

    process = await asyncio.create_subprocess_exec(
        'python',
        '14-username.py',
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE
    )

    stdout, stderr = await process.communicate(b'Amir Shariati')
    end = time.perf_counter()

    print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, stdout: {stdout}')
    print(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}, stderr: {stderr}')

    print('-------------------------------------------------------------')
    print(f'waiter coroutine took {end - start:.2f} second(s) to finish')


asyncio.run(main())
