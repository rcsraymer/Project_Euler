#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
import math
from itertools import combinations

expected_sum = 1000

# Divide by 3, set min vals for all
a, b, c = int((expected_sum / 3)-1), a + 1, a + 3

print(a,b,c)

ranged_lst = range(2,expected_sq)
print(ranged_lst)
for i in ranged_lst:
    sqc = math.sqrt(i)
    if i == sqc**2:
        print(i)
    else:
        pass

triples = list(combinations(ranged_lst,3))

for a,b,c in triples:
    if a + 

#
#for a,b in tuples:
#    a2 = a**2
#    b2 = b**2
#    c = a2 + b2
#    sqc = math.sqrt(c)
#    print(a2,b2,c)
#    if c == sqc**2:
#        if a2 + b2 + c == expected_sum:
#            print(a,b,int(sqc))
#            print(a2,b2,c)
#        else:
#            pass
#    else:
#        pass

print(math.sqrt(200))
