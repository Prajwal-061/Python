print(1+2*3+4)  
"""the precedence of multiplication is higher than addition, so first multiplication and then
addition so output will be 11 """

print(400>200)  # it returns the boolean value as it is compairing the two integers.
#we can make the statement of first line to be user friendly, parenthesis can be added which clarifies the user.
y=(1+(2*3))+4
print(y)
# 2%3 it means that 2 is divided by 3 and returns the value of remainder
print(1+2%3) # the modulus has higher precedence than the addition and subtraction.
print(1+(2%3)) 
print((1+2)%3)  
print( 'apple'>'Apple' ) # it returns True uppercase letter are considered as less that is case sensitivity
print( 'bacon'<'eggs' ) # it returns True because the "e" has greater ascii value than b
print( 'bacon'<'Eggs' ) # since here is uppercase, it is considered as less.
print('downgrade'<'grade') # here the asci value of the "g" is greater than the "d"
# prefix comparison
print('in'>'incomplete')
print(1+2)
print('one'+'two') # adding of the two strings gives the string that is onetwo
print(False+1) # False in boolean is 0 and 0+1 is 1

x=str(34)
y=int(45)
z=float(46)
print(type(x))
print(x,y,z)
print("line1 \nline2")




