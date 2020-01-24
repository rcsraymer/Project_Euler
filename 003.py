import math
import numpy as np

# Question
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Answer


n = 70000

s = int(math.sqrt(n) - 1)

ranged_list = list(range(2,s))
print(len(ranged_list))
filtered_list = []

# Prefilter list ... remove all divisible by 2, 3, 5, 7
x = lambda m: (m == 2 or m % 2 != 0) and (m == 3 or m % 3 != 0)
# and (m == 5 or m % 5 != 0) and (m == 7 or m % 7 != 0)
filtered_list = list(filter(x, ranged_list))

print('initial size of list',len(filtered_list))
print(filtered_list)

start = 2
end = 5
# fix start and end 
for i in filtered_list[start:end]:
    x = lambda m: (m == i or m % i != 0)
    filtered_list = list(filter(x, filtered_list))
    start = start + 3 
    end = end + 3
    print(i)
    print('size of list' , len(filtered_list))

print(filtered_list)


list_1 = list(range(200))
list_1_len = len(list_1)


start = 0
end = 5
loops = 0

while loops < list_1_len:
    for i in list_1[start:end]:
        start = start + 5
        end = end + 5
        print(i)
    
#
#
#prime_list = []
#
#ranged_list = list(range(2, s + 2))
##print(len(ranged_list))
#
#loops = 0
#
#increment = 0
#
#while loops < s in ranged_list:
#    print(loops)
#    loops += 1
#    for l in loops:
#        stuff = l * l + increment
#        print(stuff)
#        increment += 1
#
## Need to determine if numbers passed in are prime numbers
#
#
#
#
## Prefilter for 2, 3
##ranged_list = [num for num in ranged_list if ((num == 2) or (num == 3)) 
##                                or ((num % 2 != 0) and (num % 3 !=0))]
#
##prime_list = []
##
##for idx, val in enumerate(ranged_list):
##    ranged_list = [num for num in ranged_list if num == val or num % val != 0]
##    prime_list = [num for num in ranged_list if n % num == 0]
##
##print(prime_list)
