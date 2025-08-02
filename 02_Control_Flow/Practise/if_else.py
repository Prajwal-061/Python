cars=['bmw','honda','tata','toyata']
for x in cars:
    if x=="bmw":
        print(x.upper())
    else:
        print(x.title())
        
print('bmw' in cars)
print("honda \n" in cars)

# checking whether the value is in the list
users=["Perry","Tina","hela","marie",'calorine','olivia']
banned_users=['calorine','marie','hela','tina']
for user in users:
    if user  not in banned_users:
       print(user.title()+" "+ ",You are  allowed to like and comment the post.")
    else:
       print(user.title()+" "+ ",You are not allowed to like and comment the post.")
       
#simple if statement 
age=18
if age>=18:
    print("you can vote")
    print("Have you registere to vote?")
else:
    print("you are not eligible to vote")
    
age=int(input("Enter you age:"))
if age<=4:
    print(" Congratulations!!!! Admission is Free For you.")
elif age<=18:
    print("Admission cost is $5 for you.")
elif age==65:
    price=15
    print("Admission cost is"+ " " + str(price) + " " +" for you")
else:
    print("Admission cost is $10 for you.")
    
        