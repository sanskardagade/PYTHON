'''
Real-World Example: Multiprocessing for CPU-Bound Tasks
Scanerio : Calculating Factorials / Factotial Calculations
Factorial calculations, especially for large numbers, involve significant computational effort. Multiprocessing can be used to distribute the workload across multiple CPU cores, improving performance.
'''


import multiprocessing
import math
import sys 
import time


## Increase the maximum number of digits for integer conversion 

sys.set_int_max_str_digits(100000)

## function to compute factorial of a given number

def computer_factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}.")
    return result

if __name__ == "__main__":
    numbers = [2000, 3000, 4000, 5000]
    start_time = time.time()

    ## create a pool of worker process
    with multiprocessing.Pool() as pool:
        results = pool.map(computer_factorial, numbers)

    end_time = time.time()
    
    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")
