student_marks = {
    'Math': 85,
    'Science': 92,
    'English': 78,
    'History': 65,
    'Art': 55
}
total=0;
average=0
for sub in student_marks:
    print(f"Subjects:{sub} , Marks {student_marks[sub]}")
    total+=student_marks[sub]
average=total/5
print(f"the total marks is {total} \nthe average marks is {average}")

if average >=90 and average < 101:
    print("Grade:A")
elif average >= 80 and average <90:
    print("Grade:B")
elif average >= 70 and average < 80:
    print("Grade: C")
elif average >= 60 and average < 70:
    print("Grade: C")
else:
    print("Fail")
