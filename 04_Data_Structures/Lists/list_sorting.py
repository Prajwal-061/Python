# we can simply sort the list using sort() method in python and after sorting we can revert to the original form.
a=['audi','bmw','toyota','ducati']
a.sort()
print(a)

# we  can sort in reverse order by passing argument reverse = true in the sort.
a.sort(reverse=True)
print(a)

# everytime we sort the order of the list is permanently changed.
# we can reverse by this method also
b=[1,2,3,4,5,6,7]
b.sort(reverse=True)
print(b)
print('\n')
c=[13,5,2,3,73,7,1,4,8,9]
c.sort()
print(c)

# sorting the list temporarily with the sorted() function
laptops=['lenovo' , 'dell', 'acer', 'hp','msi']
print("here is the original list:",laptops)
print("here is the sorted list:",sorted(laptops))

# we can see that the original order is not changed.
print(laptops)

# we also can print in the backward order using reverse= True in the sorted()
# it actually doesnt reverse but it sorts in the reverse way.
print("here is the reversed sorted list of laptops")
print(sorted(laptops, reverse=True))
print(" we can see that original list remains unchanged :",laptops)

# printing the reverse of the list using reverse() method, it doesnot sort in reverse order but prints in reverse order.
names=['prajwal','aashish','abhinav','aayush']
# we cannot use directly print(names.reverse()) it gives output as none
print("original list of the names")
print(names)

names.reverse()
print("reversed order of the names")
print(names)

# we can find the length of the list using len() function
print(len(names))
