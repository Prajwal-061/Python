current_user = ["Prajwal", "Utsav", 'Abhinav', "Aayush", "Aashish"]
new_user = ["Sulav", "Ujjwal", "abhinav", "Aashish", "Pratik"]
new_current_user = [user.lower() for user in current_user]
for name in new_user:
    new_name = name.lower()
    if new_name in new_current_user:
        print(f"{name} ,You have to enter new user name.")
    else:
        print(f"{name} is available")



