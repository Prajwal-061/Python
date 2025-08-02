import csv
students={}
n=int(input("enter the total number of students:"))
for i in range(n):
    name=input(f"Enter the name of student {i+1}:")
    no_of_subjects=int(input("enter number of subjects for this student:"))
    subject_marks={}
    for j in range(no_of_subjects):
        sub_name=input(f"Enter the name of the subject {j+1}:")
        sub_mark=int(input(f"Enter the marks for the subject{j+1}:"))
        subject_marks[sub_name]=sub_mark
    students[name]=subject_marks
print(students)

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

with open("student_report.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write header row
    writer.writerow(["Student", "Subject", "Marks", "Status"])

    # Loop through the student data again
    for stu_name, marks in students.items():
        for subject, mark in marks.items():
            status = "Pass" if mark >= passing_mark else "Fail"
            writer.writerow([stu_name, subject, mark, status])

print("Student report exported to student_report.csv successfully!")
