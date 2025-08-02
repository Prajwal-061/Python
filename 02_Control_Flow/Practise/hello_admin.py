user_names = ["Prajwal", 'Admin']
if len(user_names) == 0:
    print("we need to find the new user")
else:
    for name in user_names:
        if name == 'admin' or name == 'Admin':
            print(f"Hello admin, Would you like to see a status report?")
        else:
            print(f"Hello {name} thank you for logging in.")
