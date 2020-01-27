#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.
from itertools import combinations as combinations

# Set start and end nums with 3 digits
start_num = 100
end_num = 999

# Create array with range of start_num -> end_num
arr = list(range(start_num, end_num))
r = 2

palindrome_lst = []

# Reverse number and check if it's a palindrome
def palindrome_check(num):
    return str(num) == str(num)[::-1]

# Use combinations from itertools library to show all unique combos in range
lst1 = list(combinations(arr, r))

# Multiply each pair in list, assign to z list
z = [x * y for x, y in lst1]

# Iterate through z and check each value. If Palindrome, add to palindrome_lst
for l in z:    
    chck = palindrome_check(l)
    
    if chck == True:
        palindrome_lst.append(l)
    
print(palindrome_lst)
print(max(palindrome_lst))
