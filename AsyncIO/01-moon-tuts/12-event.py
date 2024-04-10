import asyncio
import datetime
import time
import random
import functools


def trigger(event: asyncio.Event):
    event.set()


