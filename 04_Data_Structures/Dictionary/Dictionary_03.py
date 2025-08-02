appl_revenus={
    "USA":{
        "iphone":20,
        "ipad":12,
        "MacBook":8
    },
    "China":{
        "iphone":17,
        "ipad":9,
        "MacBook":6
    },
    "India":{
        "iphone":9,
        "ipad":4,
        "MacBook":2
    }
}


for Country,brand in appl_revenus.items():
    print(Country,brand)

for country ,product_data in appl_revenus.items():
    for product,rev in product_data.items():
        print(f"{country} {product} revenue:${rev}million")