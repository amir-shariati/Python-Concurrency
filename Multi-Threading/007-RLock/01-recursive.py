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


# Create multiple threads
threads = [Thread(target=recursive_function, args=(3,)) for _ in range(3)]

# start all threads
[thread.start() for thread in threads]

# joint all threads
[thread.join() for thread in threads]
