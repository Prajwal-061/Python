#tuple
# Simply tuple is an immutable list. that means wo cannot modify or change the tuple.
dimensions=(200,50)
print(dimensions[0])
""" dimensions[0]=250   gives the type error something like this:'tuple' object does not support item assignment"""
# looping through the tuple
for x in dimensions:
    print(x)
# writing over a tuple
#. Python doesn’t raise any errors this time, because overwriting a variable is valid:
dimensions=(200,50)
print("original dimensions:")
for dimension in dimensions:
    print(dimension)
new_dimension=(150,45)
print("Modified dimensions:")
for x in new_dimension:
    print(x)
# Error tuple has no attribute insert or modifying the value is not supported in the tuple
"""new_tuple=('Prajwal','Ujjwal')
new_tuple.insert(0,'Utsav')
print(new_tuple)"""
# Resturant menu
menu=("MOMO","Burger","Hot Dogs","Naan Roti")
print("The Resturant offers the following foods:")
for x in menu:
    print(x) 
print("\nSince the hot dogs and Naan roti remained unsold for couple of months, The Revised Menu is:")
menu=("MOMO","Burger","Pizza","KFC")
for x in menu:
    print(x)