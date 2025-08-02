"""
BITWISE OPERATORS
& -----> and
| -----> or
^ ----->XOR
~ ----->NOT(compliment)
<< ----> left shift
>> -----> right shift
"""
# bitwise and
a = 5  # 101
b = 4  # 100
print(a & b)  # 100    # gives 1 when both are 1 else return 0   # similar like and gate.

# bitwise or
a = 5  # 101
b = 4  # 100
print(a | b)  # 101   gives 0 when both are 0 else returns 1  # same like or gate

# bitwise expr
a = 5  # 101
b = 4  # 100
print(a ^ b)  # 001      # gives 0 when both bit are same else 1

# bitwise NOT
a = 5  # 0101
print(~a)  # 1010      # it reverses the bit   it always gives -(a+1).

# bitwise left shift----> we will gain the bits
a = 5  # 101
print(a << 2)  # we always get a*2^n   # here a=5,n=2 that gives (5*4=20)

# bitwise right shift-----> we will lose the bits
a = 5  # 0101
print(a >> 2)  # 0001     # we always get a/2^n  # here a=5,n=2 that gives (5/4=1)

# exercise
a = 23  # 10111
b = 26  # 11010
print(a & b)  # 10010

a = 17  # 10001
b = 24  # 11000
print(a | b)  # 11001

print(~45)
print(68 << 2)
print(56 >> 3)
