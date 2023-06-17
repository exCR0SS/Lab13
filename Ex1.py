import threading
import time

def print_time(thread_name):
    for i in range(10):
        print(thread_name, ":", time.ctime())
    time.sleep(1)

thread1 = threading.Thread(target=print_time, args=("Thread 1",))
thread2 = threading.Thread(target=print_time, args=("Thread 2",))

thread1.start()
thread2.start()