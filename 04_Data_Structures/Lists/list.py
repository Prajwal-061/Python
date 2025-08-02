# A list is the collection of items in a particular order.
# a list can contain the  values of different datatypes. it a mutable that is the assigned value can be modified.
subjects=['maths','physics','chemistry','computer']
print(subjects)

# we can acess the individual elements from the list through the index position and index starts from 0 not 1.
newspaper=['the kantipur','the gorkhapatra','the himalayan times']
oldest=newspaper[1].title()
print("The oldest newspaper of the Nepal is" , oldest)

#on has a special syntax for accessing the last element in a list. By asking for the item at index -1,
# Python always returns the last item in the list:
print(newspaper[-1].title())

# Similarly the index -2 returns the second last item from the list
print(subjects[-2].title())

# changing the elements of a list
motorcycles=['honda','herohonda','pulsar','bullet']
print(motorcycles)

motorcycles[1]='ducati'
print(motorcycles)
print(motorcycles[1])

# adding elements to the list 
# the "append()" method is used to add the new elements to the list at the last index position.

motorcycles.append('yamaha')
print(motorcycles)

# inserting the element into the list
# we use "insert()" method to insert the elements in desired position in the list.
motorcycles.insert(0,'bajaj')
print(motorcycles)

# removing the elements from the list using index position 
# we use "del()" method to remove the elements from the list.

del subjects[2]
print(subjects)

#The pop() method removes the last item in a list, but it lets you work 
#with that item after removing it

# in list comparison is done checking the single element in both of the lists.
a=[1,3,5]
b=[2,3,6,1000]
print(a>b)

#removing an item by value from the list.
c=['pen','copy','book','pencil']
print(c)
damage=c.remove('pen')
print(c)
print(damage)  # it gives the output none