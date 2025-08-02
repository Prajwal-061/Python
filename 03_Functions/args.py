def sum_all(*args): # *args allows any number of argument.
    total=0
    print(args) # converts the numbers into tuple.
    for num in args:
        total+=num
    return total


total=sum_all(1,2,3,4,10)
print(total)
