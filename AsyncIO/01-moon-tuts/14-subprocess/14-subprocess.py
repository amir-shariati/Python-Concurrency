import asyncio
import datetime
import time


async def main():

    process = await asyncio.create_subprocess_exec(
        'python',
        '14-username.py',
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE
    )

