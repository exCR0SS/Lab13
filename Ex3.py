import threading
import time

def print_even():
    for i in range(2, 11, 2):
        print(i)
        time.sleep(0.5)

def print_odd():
    for i in range(1, 10, 2):
        print(i)
        time.sleep(0.5)

thread1 = threading.Thread(target=print_even)
thread2 = threading.Thread(target=print_odd)

thread1.start()
thread2.start()