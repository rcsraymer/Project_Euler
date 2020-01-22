# Question
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Answer

number = 13195


# Need to determine if numbers passed in are prime numbers

ranged_list = list(range(2, number+1))

# Prefilter for 2, 3
ranged_list = [num for num in ranged_list if ((num == 2) or (num == 3)) 
                                or ((num % 2 != 0) and (num % 3 !=0))]

print(ranged_list)

prime_list = []

for idx, val in enumerate(ranged_list):
    ranged_list = [num for num in ranged_list if num == val or num % val != 0]
    prime_list = [num for num in ranged_list if number % num == 0]

print(ranged_list)
print(prime_list)
