#list of tuple
contacts=[('rachel',9843271941),('monica',1234987236),('joey',9845127824)]
for contact in contacts:
    if contact[0]=='monica':
        print(contact[1])


d={
    'rachel':8834519063,
    'monica':9192345678,
    'joey':984567235
}
print(d['joey'])
d.get('joey')
print(d)
# can update the phone
d['joey']=123456
print(d)
d['satya']=8888888 # adding new element to the dictionary
print(d)
del d['satya'] # deleting the element from dictionary
print(d)
print('abdul' in d)
print('rachel' in d)
dic={}
