# finding maximum,sum,average and minimum elements in the list
numbers=[1,2,3,4,5,6,7,8,9,3,5]
print(max(numbers))
print(min(numbers))
total_sum=sum(numbers)
print(total_sum)
avg=total_sum/len(numbers)
print(avg)

for n in range(1,21):
   print(n)
 
 # we print it making the list.
numbers=[value for value in range(1,21)]
print(numbers)

# alternative
numbers=list(range(1,21))
print(numbers) 

"""numbers = list(range(1, 1000000))
print(numbers)
print(min(numbers))
print(max(numbers))
total_sum = sum(numbers)
print(total_sum)"""

# list of the odd numbers using range() => list comprehensions
numbers=[value for value in range(1,20,3)]
print(numbers)

# other way using loop
number=[]
for value in range(1,20,3):
    number.append(value)
print(number)  

#other way
numbers=list(range(1,20,3))
print(numbers)

#  list of multiples of 3 using for loop
multiple_3=[]
for value in range(3,31,3):
    multiple_3.append(value)
print(multiple_3)
 
# alternative using list comprehension
multiple_3=[value for value in range(3,31,3)]
print(multiple_3)

# creating list to print the odd numbers from 1 to 20 using comprehension list
odd_numbers=[value for value in range(1,21,2)]
print(odd_numbers)

# using slicing in the loop
names=['ram','shyam','hari','krishna','radha']
for name in names[1:4]:
    print(name.title()+" "+" is a goood student.")

#here only one 2 gets removed.
""" Here's how the iteration goes:
The first element is 1, nothing happens.
The second element is 2, it's removed. The list becomes [1, 2, 4, 5].
The third element is now 4 (because the list shifted), nothing happens.
The fourth element is 5, nothing happens."""
numbers=[1,2,2,4,5]
for i in numbers:
    if i==2:
       numbers.remove(i)
print(numbers)      

""" we can solve it by using list comprehension"""  
"""numbers=[1,2,2,4,5]
numbers=[value for value in numbers if value==2 numbers.remove(value)] 
You will encounter a SyntaxError because the syntax if value == 2 numbers.remove(value) is not valid.
You cannot have an expression (such as numbers.remove(value)) directly within the list comprehension condition.
The condition should be a boolean expression, and modifications to the list should occur outside the list 
comprehension."""

numbers = [1, 2, 2, 4, 5]
numbers = [value for value in numbers if value != 2]
print(numbers)


