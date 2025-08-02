students = {
    "Ram": {"Math": 80, "English": 75, "Science": 70},
    "Sita": {"Math": 90, "English": 85, "Science": 95},
    "Gita": {"Math": 70, "English": 65, "Science": 60}
}

for name,marks in students.items():
    total = 0
    for subjects,mark in marks.items():
        total+=mark
    average=total/3
    print(f"{name}: Average = {average}")