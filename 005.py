# Question:
#2520 is the smallest number that can be divided by each of the numbers 
#from 1 to 10 without any remainder.
#
#What is the smallest positive number that is evenly divisible by all of the 
#numbers from 1 to 20?

# Answer: 232792560

# TODO @ 4:42 : Research Least common multiple

import time

start = time.time()

range_num = 25
inc_num = range_num

chk_lst = list(range(2, range_num+1))

# Prefilter list ... only primes should remain
# For a max range num of 20, there is no reason to have 2, 4, 5, etc
for l in chk_lst:
    chk_lst = [num for num in chk_lst if num == l or l % num != 0]

div_even = False

while div_even == False:
    if inc_num % (range_num - 1) == 0:
        z = [inc_num % l for l in chk_lst]
        if sum(z) == 0:
            div_even = True
        else:
            inc_num = inc_num + range_num
    else:
        inc_num = inc_num + range_num
    
print(inc_num)
print(div_even)

end = time.time()
print(end - start)

# answer is 232792560
# make it faster.
