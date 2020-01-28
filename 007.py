#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
#What is the 10 001st prime number?
import time
start = time.time()

chunk_by = 500
inc_num = 2

prime_lst = [inc_num]


while len(prime_lst) != 300:
    
    inc_num = inc_num + 1    
    prime_lst.append(inc_num)
    
    for i in prime_lst:
        x = lambda m: (m == i or m % i != 0)
        prime_lst = list(filter(x, prime_lst))

print(prime_lst)
print(prime_lst[-1])


end = time.time()
print(end - start)
