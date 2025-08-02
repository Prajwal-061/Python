for n in range(1,21):
    print(n)
    
#list comphrension
numbers=[x for x in range(2,21,2)]
print(numbers)

odd_number=[x for x in range(1,20,2)]
print(odd_number)

# other ways
numbers=list(range(1,21))
print(numbers)

numbers=[]
for value in range(1,21,3):
    numbers.append(value)
print(numbers)

even_numbers=[x for  x in range(2,51,2)]
print(even_numbers)

natural_numbers=[]
for x in range(1,20):
    natural_numbers.append(x)
print(natural_numbers)

names=["Prajwal","Utsav","Ujjwal","Tara","Uttam"]
for x in names:
    print(x,"is the family")
    
#using slicing in the loop
names=["Prajwal","Utsav","Ujjwal","Tara","Uttam"]
for x in names[1:3]:
    print("hello",x)
    
check=[1,2,3,3,4]
for x in check:
    if x==3:
        check.remove(x)
print(check)
    
check=[value for value in check if value !=3]
print(check)

numbers=[1,2,3,4,5]
for x in range(1,6):
    square=x**2
    numbers.append(square)
print(numbers)


numbers=[1,2,3,4,5,6,7]
square=[]
for x in numbers:
    square.append(x**2)
    numbers=square
print(numbers)

#easy method using list comphrenison
original_list=[1,2,3,4,5,6,7,8]
original_list=[value**2 for value in original_list]
print(original_list)

#copying the list usinf slicing
my_list=["hi","bye","hello","meow"]
friend_list=my_list[:]
print(friend_list)
my_list.append("hoho")
friend_list.append("hawa")
print(friend_list)
print(my_list)

for x in my_list[1:3]:
    print(x)
    