## Multiprocessing in Python
## Processes that run in parallel 
## When to use multiprocessing 
# CPU-bound tasks : Tasks that are heavy in CPU usage (e.g, mathematical computations, complex calculations, data processing).
# Parallel execution : Multiple cores can be utilized to perform tasks simultaneously, improving performance for CPU-intensive operations.(Multiple cores of cpu can be utilized)



import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i * i}")


def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i * i * i}")

if __name__ == "__main__":     ## This is just to give the entry point for the program
    ## Create two processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)
    t = time.time()

    ## Start the process
    p1.start()
    p2.start()

    ## Wait for both processes to complete
    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(finished_time)
