# unpacking in the context of programming rfers to the extracting individual elements from a container such as 
# list, tuple... and assigning them to the separate variable.
# the * operators can be used for unpacking iterables.
a,b,*_=[1,2,3,4,5]
print(_)
print(a)

*x,y,z=[1,2,3,4,5,6,7]
print(x)
print(y)

# we cannot use more than one unpacking operator in a single list.
# error=>> multiple starred expressions in assignment
"""*x,*y,z=['apple','bananna','pineapple','mango']"""

# value Error
"""p,q,r=10,23,34,45"""

# cannot assign the value to true
# syntax error, True is a built in fucntion to the python
"""True = False
False=True
print(not True,not False)"""

#cpython
l=[[]]*4
l[0].append('hello')
print(l)