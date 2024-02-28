from threading import Thread, RLock, current_thread

# Create a reentrant lock
lock = RLock()


def recursive_function(count):
    # Acquire the lock
    lock.acquire()
    print(f"Thread {current_thread().name} acquired lock: count={count}")
    if count > 0:
        # Call the function recursively
        recursive_function(count - 1)
        # Release the lock
    lock.release()
