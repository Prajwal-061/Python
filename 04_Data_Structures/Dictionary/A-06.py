students = {
    "Ram": {"Math": 80, "English": 75},
    "Sita": {"Math": 90, "English": 85},
    "Gita": {"Math": 70, "English": 65}
}

for name,marks in students.items():
    print(f"{name}:")
    for subjects,mark in marks.items():
        print(f" {subjects}:{mark}")