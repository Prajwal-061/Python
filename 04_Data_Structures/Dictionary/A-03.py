inventory={
    'pen':10,
    'notebook':5,
    "eraser":15,
    "pencil":0
}

customer_requests=['pencil',"marker","notebook","pen"]
for item in customer_requests:
    if item in inventory and inventory[item]>0:
        print(f"Item {item} is availabe")
    elif item in inventory and inventory[item]==0:
        print(f"Item {item} is out of stock")
    else:
        print(f"Item {item} is not sold here")

