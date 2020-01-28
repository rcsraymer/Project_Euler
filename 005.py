# Question:
#2520 is the smallest number that can be divided by each of the numbers 
#from 1 to 10 without any remainder.
#
#What is the smallest positive number that is evenly divisible by all of the 
#numbers from 1 to 20?

# Answer: 232792560
import time

start = time.time()

# Set Range Max and Incrementing # 
range_num = 24
inc_num = range_num

# Create a list with a range of 2 - max (range-num) + 1
chk_lst = list(range(2, range_num+1))

# Prefilter list ... only primes should remain
# For a max range num of 20, there is no reason to have 2, 4, 5, etc
for l in chk_lst:
    chk_lst = [num for num in chk_lst if num == l or l % num != 0]

# Determine loop starting point.This is used within the while statement below. 
# Bc the inc_num is incremented by the range_num, inc_num is always divisible by range_num
# The filtering can be sped up by getting the next to last element in the chk_lst
div_loop_num = chk_lst[-2] if len(chk_lst) > 1 else range_num

# If division by all #s is 0 then set True. Default = False 
div_even = False

while div_even == False:
    
    # Check if num incremented is divisible by next to last element in chk_lst    
    if inc_num % div_loop_num == 0:
        
        # If so, inc_num % l in list comprehension
        z = [inc_num % l for l in chk_lst]
        
        # If sum of list is 0 set div_even to true to break the loop else increment inc_num
        if sum(z) == 0:
            div_even = True
        else:
            inc_num = inc_num + range_num
    
    # Increment inc_num while div_even is False
    else:
        inc_num = inc_num + range_num
    
print(inc_num)
end = time.time()
print(end - start)
