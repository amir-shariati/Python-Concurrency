"""
If you want to achieve the same behavior as RLock without using the threading.RLock() object, you can use a regular Lock
object and track the owner of the lock manually. Here's an example that achieves the desired behavior.

In this modified example, I created a custom ReentrantLock class that uses a regular Lock object internally.
It keeps track of the lock owner and a counter to mimic the reentrant behavior.

By using this custom ReentrantLock class, you can achieve the same behavior as RLock where a thread can acquire the lock
multiple times without causing a deadlock.
"""

import threading


class ReentrantLock:
    def __init__(self):
        self.lock = threading.Lock()
        self.owner = None
        self.counter = 0

    def acquire(self):
        current_thread = threading.current_thread()
        if self.owner == current_thread:
            # If the current thread already owns the lock, increment the counter
            self.counter += 1
        else:
            # Acquire the lock and set the owner
            self.lock.acquire()
            self.owner = current_thread
            self.counter = 1

    def release(self):
        if self.owner != threading.current_thread():
            raise RuntimeError("Lock can only be released by the owning thread.")
        self.counter -= 1
        if self.counter == 0:
            # Release the lock if the counter reaches zero
            self.owner = None
            self.lock.release()


# Create a reentrant lock
lock = ReentrantLock()


def recursive_function(count):
    # Acquire the lock
    lock.acquire()
    print(f"Thread {threading.current_thread().name} acquired lock: count={count}")
    if count > 0:
        # Call the function recursively
        recursive_function(count - 1)
    # Release the lock
    lock.release()


# Create multiple threads
threads = [threading.Thread(target=recursive_function, args=(3,)) for _ in range(3)]

# start all threads
[thread.start() for thread in threads]

# Wait for all threads to finish
[thread.join() for thread in threads]

print(f'Done!')
