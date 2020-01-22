# Question
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Solution
# Use the modulus operator to find where i in range of 1000 has no remainder when divisible by 3 or 5
# Add only those values to a list
# Sum the list

lst = []

for i in range(1000):
    if ((i % 3 == 0) or (i % 5 == 0)):
        lst.append(i)
    
print(sum(lst))

## 233168 is the sum