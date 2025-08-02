#Print characters from a string that are present at an even index number
name="PYNATIVE"
size=len(name)
for i in range(0,size-1 ,2):
        print(name[i])
print("\n")
# using list slicing
x=list(name)
for i in x[0::2]:
    print(i)
print("\n")
        
# next method
name=input("enter your name:")
for i in range(len(name)):
    if i%2==0:
        print(name[i])