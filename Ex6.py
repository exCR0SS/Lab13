import threading

def sum_numbers(numbers):
    total = sum(numbers)
    print("Sum:", total)

numbers = [1, 5, 2, 6, 3, 8, 4, 9, 7, 10]
num_threads = threading.cpu_count()

threads = []
for i in range(num_threads):
    start_index = i * len(numbers) // num_threads
    end_index = (i+1) * len(numbers) // num_threads
    thread = threading.Thread(target=sum_numbers, args=(numbers[start_index:end_index],))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()