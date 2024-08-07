# 1. Creating Thread
# 2. Daemon Thread
# 3. Sychronization
# 4. Thread Pool Executor
# 5. Global Interpretor Lock 

# 1. Thread Example

import threading
import time

# Define a function that will be run by each thread
def worker(thread_name):
    print(f"Thread {thread_name} starting.")
    time.sleep(2)  # Simulate a time-consuming task
    print(f"Thread {thread_name} finished.")

# Create threads
thread1 = threading.Thread(target=worker, args=("A",))
thread2 = threading.Thread(target=worker, args=("B",))

# Start the threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("Both threads have finished execution.")

# -------------------------------------------------------------------------------------------------------------------------------

# 2. Daemon Thread 

# Daemon threads in Python are threads that run in the background and are terminated automatically when the main program exits, 
# even if they haven't completed their execution.

import threading
import time

def daemon_worker():
    while True:
        print("Daemon thread is running...")
        time.sleep(1)

def non_daemon_worker():
    for i in range(5):
        print("Non-daemon thread is running...")
        time.sleep(1)

# Create and start daemon thread
daemon_thread = threading.Thread(target=daemon_worker, daemon=True)

# Create and start non-daemon thread
non_daemon_thread = threading.Thread(target=non_daemon_worker)

# Start threads
daemon_thread.start()
non_daemon_thread.start()

# Wait for the non-daemon thread to complete
non_daemon_thread.join()

print("Non-daemon thread has finished execution.")
print("Main program is ending...")

# At this point, the daemon thread will be stopped as the main program exits

# When you run this code, you should see the non-daemon thread output its messages 5 times, while the daemon thread keeps printing its 
# message every second. After the non-daemon thread completes, the main program exits, and the daemon thread is stopped automatically, 
# even if it is still running.

# ---------------------------------------------------------------------------------------------------------------------------------------

# 3. Synchronization

# Thread synchronization in Python is crucial when you have multiple threads accessing shared resources to prevent race conditions and ensure
# data consistency. Python provides several mechanisms for synchronization in the threading module, such as locks, events, semaphores, and 
# conditions.

# 3.1 locks

# Locks are the most basic synchronization mechanism. They are used to ensure that only one thread can access a critical section of code at a time.

import threading
import time

# Shared resource
counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:
        # Critical section
        local_counter = counter
        time.sleep(0.1)  # Simulate some work
        counter = local_counter + 1

threads = []

# Create and start threads
for _ in range(10):
    t = threading.Thread(target=increment)
    t.start()
    threads.append(t)

# Wait for all threads to finish
for t in threads:
    t.join()

print(f"Final counter value: {counter}")


# 3.2 Events 

# Events are used for signaling between threads. An event is essentially a flag that can be set or cleared. 
# Threads can wait for the event to be set before proceeding.

import threading
import time

event = threading.Event()

def waiter():
    print("Waiting for event to be set...")
    event.wait()  # Block until the event is set
    print("Event is set! Proceeding...")

def setter():
    time.sleep(2)
    print("Setting the event...")
    event.set()

# Create and start threads
t1 = threading.Thread(target=waiter)
t2 = threading.Thread(target=setter)

t1.start()
t2.start()

t1.join()
t2.join()

# 3.3 Semaphores

# Semaphores are used to control access to a shared resource by limiting the number of threads that can access it simultaneously.

import threading
import time

semaphore = threading.Semaphore(2)  # Allow up to 2 threads to access at the same time

def task():
    print(f"{threading.current_thread().name} attempting to acquire semaphore...")
    with semaphore:
        print(f"{threading.current_thread().name} acquired semaphore.")
        time.sleep(2)
    print(f"{threading.current_thread().name} released semaphore.")

threads = []

# Create and start threads
for i in range(5):
    t = threading.Thread(target=task, name=f"Thread-{i+1}")
    t.start()
    threads.append(t)

# Wait for all threads to finish
for t in threads:
    t.join()

# 3.4 Conditions 

# Conditions are used for complex thread synchronization. They allow threads to wait until a certain condition is met.

import threading
import time

condition = threading.Condition()
data_ready = False

def producer():
    global data_ready
    time.sleep(2)  # Simulate data production
    with condition:
        data_ready = True
        print("Data is ready, notifying consumers...")
        condition.notify_all()

def consumer():
    with condition:
        while not data_ready:
            print(f"{threading.current_thread().name} waiting for data...")
            condition.wait()
        print(f"{threading.current_thread().name} received data!")

# Create and start threads
producer_thread = threading.Thread(target=producer)
consumer_threads = [threading.Thread(target=consumer, name=f"Consumer-{i+1}") for i in range(3)]

producer_thread.start()
for t in consumer_threads:
    t.start()

producer_thread.join()
for t in consumer_threads:
    t.join()
"""
Explanation:
Locks: Used to ensure exclusive access to a shared resource.
Events: Used for signaling between threads.
Semaphores: Limit the number of threads that can access a resource concurrently.
Conditions: Used for more complex synchronization based on conditions.
"""
