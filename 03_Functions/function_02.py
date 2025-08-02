import math

expenses=[10,25,64,100]
print(math.sqrt(expenses[3]))
def square(a):
    return a*a

x=square(5)
print(x)

# easiest way or using lambda function
# x= lambda a,b:a+b
# print(x(5))

age= int(input("enter the age:"))
can_drive=lambda y:"you can drive" if x> 18 else "You cannot."
print(can_drive(age))