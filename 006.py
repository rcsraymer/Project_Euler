#The sum of the squares of the first ten natural numbers is,
#
#1^2+2^2+...+10^2=385
#The square of the sum of the first ten natural numbers is,
#
#(1+2+...+10)^2=55^2=3025
#Hence the difference between the sum of the squares of the first ten natural 
#numbers and the square of the sum is 3025−385=2640.
#
#Find the difference between the sum of the squares of the first one hundred 
#natural numbers and the square of the sum.

# Answer : 25164150

# Set count limit and create ranged list
nat_num_cnt = 100
rng_lst = list(range(1, nat_num_cnt+1))

# Set the sum of the squares
sum_sq = sum([r**2 for r in rng_lst])

# Set the square of the sum
sq_sum = sum([r for r in rng_lst])**2

# Find diff between
diff_btwn = sq_sum - sum_sq

print(diff_btwn)
