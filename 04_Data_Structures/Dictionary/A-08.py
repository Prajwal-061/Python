students = {
    "Ram": {"Math": 80, "English": 75, "Science": 70},
    "Sita": {"Math": 90, "English": 85, "Science": 95},
    "Gita": {"Math": 70, "English": 65, "Science": 60}
}
sub=students["Ram"]
for subject in sub:
    highest = 0
    topper= ""
    for name in students:
      subject_mark=students[name][subject]
      if subject_mark  > highest:
          highest=subject_mark
          topper=name

    print(f"{subject}:{topper} scored {highest}")