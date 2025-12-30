### Multithreading 
### When to use Multithreading
### I/O - bound tasks : Tasks that spend more time waiting for I/O operations. (e.g, file operations, network requests).
### Concurrent execution : When you want to imporove the throughput of your application by performing multiple tasks concurrently.



import threading
import time

def print_numbers():
    for i in range (5):
        time.sleep(2)
        print(f"Number: {i}")

def print_letters():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")

##Create two threads
t1 = threading.Thread(target = print_numbers)
t2 = threading.Thread(target = print_letters)
    
# t = time.time()
# print_numbers()
# print_letters()
# finised_time = time.time() - t
# print(finised_time)

t = time.time()
t1.start()
t2.start()  
### Wait for both threads to complete
t1.join()
t2.join()
finised_time = time.time() - t
print(finised_time)