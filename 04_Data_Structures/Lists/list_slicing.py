import this

names=['Prajwal','Uttam','Tara']
print(names)
print("\n")

# modifying the lements in the list
names[0]='Ujjwal'
print(names)

# adding elements to the  end of the list
names.append('Ram')
print(names)

#inserting elements to the list at desired position
names.insert(3,'Prajwal')
print(names)

# deleting the names from the desired position.
del names[-1]
print(names)

#The pop() method removes the last item in a list, but it lets you work 
#with that item after removing it
motorcycles=['honda','ducati', 'pulsar','yamaha']
print(motorcycles)

# here using the "pop()"" method also deletes the last elements from the list but still we can acess the 
# deleted element

popped_motorcycles=motorcycles.pop()
print(motorcycles)
print("The last motorcycle i bought was a ",popped_motorcycles +".")

# we can pop the elements form any postion using the index inside the parenthesis of pop().
popped_motorcycles1=motorcycles.pop(0)
print(motorcycles)
print("the first motorcycle that i bought was",popped_motorcycles1+'.')

#simple rotating the list elements
num=[1,2,3,4,5,6,7]
pop1=num.pop()
pop2=num.pop()
pop3=num.pop()
print(num)
num.insert(0,pop1)
num.insert(0,pop2)
num.insert(0,pop3)
print(num)

# slicing
 #In Python, "slicing" is a way to extract a subset of elements from a list
 #(or other sequence types like strings, tuples, and arrays).
""" my_list[start:stop:step]"""

numbers=[1,2,3,4,5,6,7,8]
print(numbers[3::-2])
print(numbers[1:5])
print(numbers[1::-1])
print(numbers[::3])
 # reverse the elements in the list
print(numbers[::-1])
# other method to reverse the array elements
numbers.reverse()
print(numbers)

#In Python, when you assign a sequence (such as a list) to a slice of another sequence 
# (such as a list), Python will automatically adjust the size of the list to accommodate the new elements.
mylist=[1,2,3,4]
mylist[1:3]=[0,0,0]
print(mylist)
print(len(mylist))


new_list=[2,4,6,8,10,12,14,16,18,20]
print(new_list[1:4:2])
print(new_list[0:8:3])
print(new_list[1:3])


