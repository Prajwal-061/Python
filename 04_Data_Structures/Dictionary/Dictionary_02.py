contact_d={
    'rachel':{'phone':1234, 'address':'1 blue st','number':8888888},
    'joey':{'phone':999,'address':'& newton bivd','number':9999999}

}

print(contact_d['rachel'])
print(contact_d['rachel']['address'])

#only returns the key of the dictionary
for name in contact_d:
    print(name)

# prints all the dictionary
for name in contact_d.items():
    print(name)
print(contact_d.keys())
print(contact_d.values())