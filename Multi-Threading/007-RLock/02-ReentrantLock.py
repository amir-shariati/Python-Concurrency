"""
If you want to achieve the same behavior as RLock without using the threading.RLock() object, you can use a regular Lock
object and track the owner of the lock manually. Here's an example that achieves the desired behavior.

In this modified example, I created a custom ReentrantLock class that uses a regular Lock object internally.
It keeps track of the lock owner and a counter to mimic the reentrant behavior.

By using this custom ReentrantLock class, you can achieve the same behavior as RLock where a thread can acquire the lock
multiple times without causing a deadlock.
"""

import threading


