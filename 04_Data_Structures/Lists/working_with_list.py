magicians=['david','alice','carolina']
# here in the for loop all the values of magicians is stored in the magician and prints is one by one.
for magician in magicians:
    print(magician.title() +  ' ' ',it was a great trick') 
    print("I can't wait to see your next trick" +" " +magician.title() +'\n')
print("Thank you everyone!!. It was a great magic show.\n")

animals=['dog','cat','goat']
for animal in animals:
    print(animal.title()+" "+'would make a great pet.')
print("Any of the animals would make a great pet.")

# using the range() function.
for values in range(1,5):  # it prints from 1 to 4 
    print(values)
    
# using range() to make a list of numbers using list() function.
# the range function here starts from 1 and ends at 5 where as the list function makes it to the list.
numbers=list(range(1,6))
print(numbers)

numbers=list(range(1,7))
print(numbers)

#we can also use the range() function to skip the numbers is given range.
#In this example, the range() function starts with the value 1 and then 
#adds 2 to that value. It adds 2 repeatedly until it reaches or passes the end 
#value, 10, and produces this result
numbers=list(range(1,10,2))
print(numbers)

even_numbers=list(range(2,50,2))
print(even_numbers)


numbers=[1,2,3,4,5]
for value in range(1,9):
    square=value**2
print(numbers.append(square)) 
print(min(numbers)) # to print the minimum number present in the list
print(max(numbers)) # to print the maximum number present in the list
print(sum(numbers)) # to print the sum of the numbers present in the list


numbers=[]
for value in range(1,11):
    numbers.append(value**3)
print(numbers)

# here first we created the empty list then we squared the original list then replace the original list with the 
# squared list
numbers=[1,2,3,4,5]
squared=[]
for number in numbers:
    squared.append(number**2)
numbers=squared
print(numbers)

# we can also do it using list comprehension directly
original_list=[2,3,4,5,6,7]
original_list=[value**2 for value in original_list]
print(original_list)

#list comprehension
squares=[value**2 for value in range(1,11)]
print(squares)

# copying the list using slicing.
my_food=['momo','chowmein','burger','chicken roll','Kfc']
friend_food=my_food[:]
print("My favourite foods are\n",my_food)
print("My  friends favourite foods are\n",friend_food)

my_food.append("Nan roti")
friend_food.append("Paneer")
print("\nupdated food of  mine is",my_food)
print("\nupdated food of my friend is",friend_food)
    
list=['RealMe','Huwaei','MI','Apple','Samsung','Vivo','Oneplus','Oppo','Nokia']
print("the first three brands in the list are:",list[0:3])
print("the middle three brands in the list are:",list[3:6])
print("the last three brands in the list are:",list[6:9])

#other ways
print('\nthe first three brands are')
for x in list[0:3]:
    print(x)
    
print('\nthe middle three brands are')
for x in list[3:6]:
    print(x)
    
print('\nthe last three brands are')
for x in list[6:9]:
    print(x)
    

my_team=['RCB','CSK','RR','DC','SRH']
friend_team=my_team[:]
print(my_team)
print(friend_team)
friend_team.append('MI')
print("The Updated team of the friend is:\n",friend_team)
my_team.append('LSG')
print("The updated team of mine is:\n",my_team)

print("you can see that there two differen list for my team and for my friend team:\n")
print("my team goes like this:")
for value in my_team:
    print(value)
    
print("\nmy  friend team goes like this:")
for value in friend_team:
    print(value)