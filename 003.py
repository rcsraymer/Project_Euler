import math
import numpy as np

# Question
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Answer

#The sieve of Eratosthenes can be expressed in pseudocode, as follows:[7][8]
#
#algorithm Sieve of Eratosthenes is
#    input: an integer n > 1.
#    output: all prime numbers from 2 through n.
#
#    let A be an array of Boolean values, indexed by integers 2 to n,
#    initially all set to true.
#    
#    for i = 2, 3, 4, ..., not exceeding √n do
#        if A[i] is true
#            for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n do
#                A[j] := false
#
#    return all i such that A[i] is true.


n = 1000

s = int(math.sqrt(n))
#print(s)
prime_list = []

ranged_list = list(range(2, s + 2))
#print(len(ranged_list))

loops = 0

increment = 0

while loops < s in ranged_list:
    print(loops)
    loops += 1
    for l in loops:
        stuff = l * l + increment
        print(stuff)
        increment += 1

# Need to determine if numbers passed in are prime numbers


# Prefilter for 2, 3
#ranged_list = [num for num in ranged_list if ((num == 2) or (num == 3)) 
#                                or ((num % 2 != 0) and (num % 3 !=0))]

#prime_list = []
#
#for idx, val in enumerate(ranged_list):
#    ranged_list = [num for num in ranged_list if num == val or num % val != 0]
#    prime_list = [num for num in ranged_list if n % num == 0]
#
#print(prime_list)
