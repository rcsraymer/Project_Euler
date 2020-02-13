# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# Answer is 104743

import time
import math

start = time.time()

# Determine number of primes
prime_count = 10001

# Empty list to store primes
prime_lst = []

# Initialize increment number to first natural prime
inc_num = 2

# If length of prime_lst is less than prime_count, go
while len(prime_lst) < prime_count:
    
    # If iteration_count > 0, current inc_num not added to prime_lst
    iteration_count = 0
    
    # We only test whether num is divisible up to the square root of the num
    s = int(math.sqrt(inc_num))
    
    # Create list with range of 2 -> s + 1
    chk_lst = list(range(2, s+1))
    
    # For each num in chk_lst, see if inc_num % num in list does not have remainder
    # If no remainder: pass else add 1 to iteration_count and pass loop
    for i in chk_lst:
        if iteration_count == 0:
            if (inc_num % i != 0):
                pass
            else:
                iteration_count =+ 1
        else:
            pass
    
    # Only add inc_num to prime_lst if iteration_count == 0
    if iteration_count == 0:
        prime_lst.append(inc_num)
    else:
        pass
    
    # Increment inc_num by 1
    inc_num = inc_num + 1

print(prime_lst)
end = time.time()
print(end - start)

# 1.3029999733 second execution
