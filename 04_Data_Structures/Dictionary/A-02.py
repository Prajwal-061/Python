fruit_prices={
    "apple":100,
    "banana":40,
    "mango":150,
    "grape":90
}
print("before deleting banana")
print(fruit_prices)
fruit_prices.pop("banana")
print("after deleting banana")
print(fruit_prices)

del fruit_prices['grape']
print("after deleting grape")
print(fruit_prices)

print("the price of a mango is ",fruit_prices.get('mango'))
print(fruit_prices.get('orange',"Not availabe"))

fruits_to_check=['apple','kiwi']
for fruit in fruits_to_check:
    if fruit in fruit_prices:
        print(f"{fruit} is availabe")
    else:
        print(f"{fruit} is not availabe")