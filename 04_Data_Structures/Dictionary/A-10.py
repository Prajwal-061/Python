students = {
    "Ram": {"Math": 80, "English": 75, "Science": 70},
    "Sita": {"Math": 90, "English": 85, "Science": 95},
    "Gita": {"Math": 70, "English": 65, "Science": 60}
}
lowest = 1000
lowest_name= ""
for name,marks in students.items():
    total=0
    for subjects,mark in marks.items():
        total+=mark
    print(f"total marks of {name} is {total}")
    if total<lowest:
        lowest=total
        lowest_name=name
print(f"Students with lowest total is {lowest_name} with {lowest} marks.")


