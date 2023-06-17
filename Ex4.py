import threading

def print_number(thread_num):
    print(thread_num)

for i in range(1, 11):
    thread = threading.Thread(target=print_number, args=(i,))
    thread.start()