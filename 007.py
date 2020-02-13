# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
import time
import math


start = time.time()

# Determine number of primes
prime_count = 1000

chk_lst = []

inc_num = 2

x = lambda m: (m == 2 or m % 2 != 0) and (m == 3 or m % 3 != 0)
#
#while len(chk_lst) < prime_count:
#    for i in chk_lst:
#        z = lambda m: (m == i or m % i != 0)
#        filtered_list = [num for num in list(filter(x, filtered_list)) if n % num == 0]
#       
#
#    chk_lst.append(inc_num)
#    chk_lst = list(filter(x,chk_lst))
#    inc_num = inc_num + 1

print(chk_lst)
end = time.time()
print(end - start)


prime_count = 1000
chk_lst = list(range(2, prime_count+1))
print(chk_lst)

n = 1000

s = int(math.sqrt(n))

print(s)

# Without sq root = 0.5504837036132812
# With sq root chck = 
