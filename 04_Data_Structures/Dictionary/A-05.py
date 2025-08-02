students = {
    "Alice": {"Math": 85, "Science": 92, "English": 78},
    "Bob": {"Math": 75, "Science": 65, "English": 80},
    "Charlie": {"Math": 95, "Science": 88, "English": 90}
}
total=0
average=0
for student, subjects in students.items():
  print("Student:",student)
  for subjects,marks in subjects.items():
      print(f"{subjects}:{marks}")
  total+=marks
  average=total/3
  print(f"the total marks is {total} \nthe average marks is {average}")


