students = {
    "Ram": {"Math": 80, "English": 75, "Science": 70},
    "Sita": {"Math": 90, "English": 85, "Science": 95},
    "Gita": {"Math": 70, "English": 65, "Science": 60}
}

sub= students['Ram'].keys()
print(sub)
for subject in sub:
    total=0
    for name in students:
        total+=students[name][subject]
    average=total/len(students)
    print(f"{subject}:{average}")
