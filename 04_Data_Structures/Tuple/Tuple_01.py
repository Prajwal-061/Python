expenses=[1200,1400,1700]
point=(5,6)
print(point[0])
print(point[1])
print(type(point))



def find_pe_and_pb(price,eps,book_value):
    pe=price/eps
    pb=price/book_value
    return [pe,pb] # we can return list


value=find_pe_and_pb(100,2,4)
for val in value:
    print(val)
