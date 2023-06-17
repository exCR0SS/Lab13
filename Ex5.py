import threading

def find_max(numbers):
    max_num = max(numbers)
    print("Max number:", max_num)

numbers = [1, 5, 2, 6, 3, 8, 4, 9, 7, 10]
num_threads = threading.cpu_count()

threads = []
for i in range(num_threads):
    start_index = i * len(numbers) // num_threads
    end_index = (i+1) * len(numbers) // num_threads
    thread = threading.Thread(target=find_max, args=(numbers[start_index:end_index],))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()