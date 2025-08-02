student_score = {}


with open("student_scores.csv", "r") as f:
    next(f)  # Skip the header line
    for line in f:
        name, sub, score = line.split(",")
        score = int(score.strip())
        if name not in student_score:
           subject_marks = {}
           subject_marks[sub] = score
           student_score[name] = subject_marks
        else:
           student_score[name][sub] = score
print(student_score)

for name,marks in student_score.items():
    total=0
    highest = 0
    lowest = 100
    for sub,mark in marks.items():
        total+=mark
        if mark>highest:
            highest=mark
        if mark<lowest:
            lowest=mark
    average=total/len(marks)
    print(f"Average:{average}")
    print(f"{name}: Highest:{highest}")
    print(f"{name}: Lowest:{lowest}")
    print(f"Total:{total}")
    print("\n")
