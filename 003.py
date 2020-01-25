import math

# Question
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Answer 6857

print('Enter a number to find its largest prime factor:')

n = int(input())

s = int(math.sqrt(n) - 1)

ranged_list = list(range(2,s))
filtered_list = []

x = lambda m: (m == 2 or m % 2 != 0) and (m == 3 or m % 3 != 0)
filtered_list = list(filter(x, ranged_list))

for i in filtered_list:
    x = lambda m: (m == i or m % i != 0)
    filtered_list = [num for num in list(filter(x, filtered_list)) if n % num == 0]

print('The list of prime factors:')
print(filtered_list)
print('The largest prime factor is',max(filtered_list))
