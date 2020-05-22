#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
expected_sum = 1000

def pyth_triplets():
    for a in range(1,expected_sum):
        for b in range(1,expected_sum):
            c = expected_sum-a-b # find the third number by subtracting a and b from expected_sum, this shortens the loop
            if (a**2 + b**2) == c**2:
                return a,b,c

a,b,c = pyth_triplets()
print(a,b,c)
print(a**2,b**2,c**2)
print(a*b*c)
