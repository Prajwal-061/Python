students = {
    "Ram": {"Math": 80, "English": 75, "Science": 70},
    "Sita": {"Math": 90, "English": 85, "Science": 95}
}

highest=0
highest_name=""
lowest=1000
lowest_name=""
for stu_name,marks in students.items():
    total=0
    for subjects,mark in marks.items():
        total+=mark
    average=total/len(marks)
    print(f"{stu_name}:Total:{total}:Average={average}")
    if total > highest:
        highest = total
        highest_name = stu_name
    if total < lowest:
        lowest = total
        lowest_name = stu_name
print(f"Highest:{highest_name}({highest})")
print(f"Lowest:{lowest_name}({lowest})\n")

passing_mark=40
for stu_name,marks in students.items():
    print(f"{stu_name}")
    for subject,mark in marks.items():
        if mark>=passing_mark:
            print(f"{subject}-->Pass")
        else:
            print(f"{subject}-->Fail")
    print("\n")


