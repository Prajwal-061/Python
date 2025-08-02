guest_list=['Prativa','Prajwal','Ujjwal','Prabhat']
print(guest_list)
print("         INVITATION TO THE DINNER    ")
print("you are invited to the dinner"+ " " + guest_list[0])
print("you are invited to the dinner"+ " " + guest_list[1])
print("you are invited to the dinner"+ " " + guest_list[2])
print("you are invited to the dinner"+ " " + guest_list[3])
print(guest_list[1]+" cannot attend the dinner due to some problems so his replacement is done inviting utsav")
print('\n')
replacement=guest_list[1]='Utsav'
print('      NEW SET OF INVITATION    ')
print("you are invited to the dinner"+ " " + guest_list[0])
print("you are invited to the dinner"+ " " + guest_list[1])
print("you are invited to the dinner"+ " " + guest_list[2])
print("you are invited to the dinner"+ " " + guest_list[3])

print("\n We found the bigger dinning table,so more space is available resulting to the more guests \n")
guest_list.insert(2,'Nasana')
guest_list.insert(3,'Tara')
guest_list.append('Uttam')
for x in guest_list:
    print("you  are invited to the dinner",x)
    
print("We just found that there is only two spaces available for dinner")
print(guest_list)

# whencer we remove the elements from the list throug the pop method the index position also changes of the 
# remaining elements in the list
pop_list0=guest_list.pop(0)
pop_list1=guest_list.pop(0)
pop_list2=guest_list.pop(0)
pop_list3=guest_list.pop(0)
pop_list4=guest_list.pop(0)

print("sorry"+ " "+ pop_list0 +" "+"we could not invite you the dinner.")
print("sorry"+ " "+pop_list1 +" "+"we could not invite you the dinner.")
print("sorry"+" "+ pop_list2 +" "+"we could not invite you the dinner.")
print("sorry"+ " "+pop_list3 +" "+"we could not invite you the dinner.")
print("sorry"+ " "+pop_list4 +" "+"we could not invite you the dinner.")

print('\n')
for x in guest_list:
    print("you are still invited to the dinner",x)
print("i am inviting", str(len(guest_list)) + " people in my dinner.")