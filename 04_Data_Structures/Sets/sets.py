# set doesn't have order of printing. indexing is not allowed in sets.
set_1 = {1, 2, 3, 4, 'jenny', 5, 6, 1}
# set_1.add("Hello")  # adding new elements to the set, we can add only immutable data like tuple and string but not list
# set_1.remove(1)   removing the elements from the set, if elements is not present then show error.
set_1.discard(65)  # remove the elements and if elements is not present then it prints the original set
# set_1.clear()  clears all the elements from set.
a = set_1.pop()  # removes any random elements from the set.
print(a)
print(set_1)  # duplicate elements are not allowed in the sets.

# to create the empty set we have to use this method only
set2 = set()
print(type(set2))
