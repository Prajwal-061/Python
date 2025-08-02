# operations in set
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {6, 7, 8, 9}

# disjoint sets--> having all the elements different or having no intersection.
print(set1.isdisjoint(set2))

# subsets
print(set1.issubset(set2))  # set1 is subset of set2 or not
print(set1 <= set2)

# superset
# set1 is said to be superset  of set2 if set1 contains every element of set2
print(set1.issuperset((set2)))
print(set1 >= set2)

# del is used to delete the set items as well as set
del set2
# print(set2)  it will give the error as set2 is already deleted.
