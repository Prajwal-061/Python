# differences
set1 = {"ram", "shyam", "hari"}
set2 = {"shyam", "gopal", "mohan"}
"""print(set1.difference((set2)))
print(set1 - set2)"""
# set1 is updated
set1.difference_update(set2)
print(set1)

# symmetric differences --> (union of two sets - intersection of two sets)
set1 = {"Krishna", "Radha"}
set2 = {"Bahubali", "Krishna", "shiva"}
set3 = {"Krishna", "murali", "shyam"}
print(set1.symmetric_difference(set2))  # only one argument passing is allowed in symmetric difference.
print(set1 ^ set2 ^ set3)

# updating the sets
set1.symmetric_difference_update(set2)
print(set1)
