monthly_sales = [42, 38, 33, 36, 40, 45]
months = ["Jan", "Feb", "March", "April", "May", "June"]
threshold = 35

for sales_amount, month in zip(monthly_sales, months):
    # print(f" {month}:{sales_amount}")
    if sales_amount < threshold:
        print(f"Sales amount {sales_amount} is less than the threshold in {month}")
        break
    else:
        print(f"Sales amount {sales_amount} is greater than the threshold in {month}")

