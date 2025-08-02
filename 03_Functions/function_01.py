def find_total(expenses):
    total=0
    for expense in expenses:
        total+=expense
    return total


expenses_sergey=[30,45,70,90]
expenses_sundar=[40,23,10,85]


total_expense_sergey=find_total(expenses_sergey)
total_expense_sundar=find_total(expenses_sundar)

print("total expenses of sergey:",total_expense_sergey)
print("total expenses of sergey:",total_expense_sundar)
print(help(find_total))
# for expense in expenses_sergey:
#     total_expense_sergey+=expense
#
# print("total expenses of sergey:",total_expense_sergey)


