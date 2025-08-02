grocery_items = {
    "Apple": 50,
    "Milk": 30,
    "Rice": 70,
    "Eggs": 10
}

cart={}
while True:
    item=input("Enter item  name to buy or 0 to finish:")
    if item == "0":
        break
    if item in grocery_items:
        quantity=int(input("Enter the quantity of the item:"))
        cart[item]=quantity
    else:
        print("Item not availabe in our store")
print(cart)

total=0
for items, quantity in cart.items():
    price=quantity*grocery_items[items]
    total+=price
print(f"The total price is {total}")
