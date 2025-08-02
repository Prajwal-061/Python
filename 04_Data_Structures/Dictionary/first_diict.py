# A dictionary in python is called the collection of key value pairs.

"""Each key is connected 
to a value, and you can use a key to access the value associated with that key. 
A key’s value can be a number, a string, a list, or even another dictionary. 
In fact, you can use any object that you can create in Python as a value in a 
dictionary."""

alien_0={'color': 'green' ,'points':5}
newpoints=alien_0['points']
print(alien_0['color'])
print(alien_0['points'])
print(f"you just earned {str(newpoints)} points! ")

# adding new key value pairs in the dictionary
alien_0['X-position']=0
alien_0['y_position']=25
print(alien_0)

print("\n")


# starting with empty dictionary
print("starting with new dictionary")
alien_1={}
alien_1['color']='yellow'
alien_1['points']='10'
print(alien_1)

#modifying values in dictionary
alien_2={'color':'Red', 'points':"15"}
print(f"The alien is {alien_2['color']}.")

print("\n")
alien_2['color']='Blue'
print(f"THe alien is now {alien_2['color']}.")


alien_3={'x-position':'0' ,'y-position':'25','speed':'medium'}
if alien_3['speed']=='slow':
    x_increment=1
elif alien_3['speed']=='medium':
    x_increment=2
else:
    x_increment=3

alien_3['x-position']= alien_3['x-position'] + str(x_increment) 
print("New position:" + str(alien_3['x-position']))
del alien_3['y-position']  # removing key value pairs
print(alien_3)
print("\n")
favourite_language={
    'prajwal':'Python',
    'Abhinav':'Java',
    'Aashish':'Javascript'
}
print(f"Prajwal's favourite language is {favourite_language['prajwal'].title()}.")



