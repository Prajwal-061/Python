# strings are immutable that the value assigned to the variable cant be modified.
x='i told my friend, "python is my favourite language!"' # this works.
print(x)

 # z="i told me friend, " python is my favourite language.""
  # y= ' i told my friend, 'python is my favourite language' '
  # we cannot use this, this is error
  
  # changing cases in the strings with methods such as title(),lower(),upper()
  # converting the first character into uppercase 
  # syntax is: variablename.title()
x= 'nasana maharjan'
y='prajwal mainali'
print(x.title())
print(y.title())
"""  The method title() appears after the variable in the print() statmenet. A method is an action that Python can 
 perform on a piece of data. The dot (.) after name in name.title() tells Python to make the title() method 
act on the variable name. 
"""

# we also can directly convert into the uppercase without storing it to the any variable.
print('ram'.title())
 
 # converting into uppercase
upper_case='prajwal mainali'
print(upper_case.upper())

# converting into lower case
lower_case="NASANA MAHARJAN"
print(lower_case.lower())

# String concatenation
first_name='nasana'
last_name='maharjan'
full_name=first_name + " " + last_name
# we just concatended the strings 
print("hello," + " " + full_name.title())

# alternative 
message="hello" + " " + full_name.upper() + " " + '!!'
print(message)

# whitespaces : any nonprinting character such as spaces, tabs and end of line symbols.
print("Python")

print("\tPython") # one tab is  equivalent to 8 spaces in python . \n is used to change the line of the string

# to remove the extra whitespaces  from the right side of the string, rstrip() function is used  and lstrip() for 
# removing from the left side
# to remove the leading and trailling whitespaces from the string from both sodes we use strip().

#Leading whitespace refers to any whitespace characters (spaces, tabs, newlines) that appear at the beginning of
# a string. Trailing whitespace refers to any whitespace characters that appear at the end of a string. 

# here when we use rstrip it only removes  to the whitespaces from the right side of the string.
language="   Javascript    "
print(language)
print(language.rstrip())

# but when we use the strip method it removes the white spaces form the both sides.
language="   Java    "
print(language)
print(language.strip())

#famous quote
y='Albert Einstien once said, "A person who never made a\n mistkae never tried anything new" '
print(y.strip()) 

famous_name="  Albert Einstien  "
message=' once said, "A person who never made a\n mistkae never tried anything new" '
print(famous_name , message)
# we also can access the individual element in string thorugh the index and also supports slicing.
print(famous_name[2])
print(famous_name[2::2])

# the len prints the total character in the string that is 19, space is also a character.
print(len(famous_name))

# here the whitespaces from the left and right side is removed so the lenght is reduced to 15 from 19.
famous_name=famous_name.strip()
print(len(famous_name))


# it automatically concatenates.
print('pyt' 'hon')
