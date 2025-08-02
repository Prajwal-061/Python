# reading a line in a text file one by one
f=open("fun.txt","r")

for line in f:
    print(line)

f.close()

# other way
with open("fun.txt","r") as f:
    for line in f:
        print(line)

#  readlines() this will create the array of that contents and print
with open("fun.txt","r") as f:
    lines=f.readlines()
    print(lines)


# writing in the file
with open("love.txt","w") as f:
    f.write("I love python\n")
    f.write("I love meditation\n")

# append in the file

with open("love.txt","a") as f:
    f.write("I tried to add something new to the file with the help of file handling in python")


with open("love.txt","a") as f:
    f.writelines([
        "\nI love C++\n",
        "I love scala"
    ])

with open("dummy.txt","w") as f:
     f.write("whatever")
import os
if os.path.exists("dummy.txt"):
    os.remove("dummy.txt")
else:
    print("File not found")
