set1 = {"Aayush", "Abhinav", "Aashish"}
set2 = {"Prajwal", "Ujjwal", "Aayush"}

# union of set
"""print(set1.union(set2))  # we can pass tuple as argument too
print(set1 | set2)  # here both the operands must be set"""

# print(set1.union(("Sulav", "Pratik")))
# print(set1 | ("Sulav", "Pratik"))  # unsupported oeprand

# updating the set elements
"""set1.update(set2)
print(set1)"""
# next method to update set
set1 |= set2
print(set1)

# intersection of sets
set1 = {"ram", "hari", "gopal", "shyam"}
set2 = {"ram", "hari", "krishna"}
print(set1.intersection(set2))
print(set1 & set2)

# update in intersection
set1.intersection_update(set2)  # gives the  result as new set by intersection of two sets set1 and set2.
print(set1)
