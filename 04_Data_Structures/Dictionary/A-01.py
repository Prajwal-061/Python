Person={
    'name':'Prajwal',
    'age':21,
    "city":"Kathmandu"
}
print(Person["name"])
print(Person["city"])


Person['hobby']='chess'
Person['age']=22
print(Person)

for val,detail in Person.items():
    print( "key:",val,Person[val])