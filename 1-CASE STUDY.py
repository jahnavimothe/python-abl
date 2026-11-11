applicants = [
    ("A101", "Anu", [88, 91, 84], 92, 180000),
    ("A102", "Balu", [75, 82, 79], 88, 220000),
    ("A103", "Charan", [90, 55, 95], 96, 150000),
    ("A104", "Divya", [80, 85, 82], 86, 240000)
]
eligible = []
for app in applicants:
    roll, name, marks, attendance, income = app
    total = sum(marks)
    percentage = total / 3
    if min(marks) >= 60 and percentage >= 75 and attendance >= 85 and income <= 250000:
        eligible.append((roll, name, percentage, attendance, income))
for i in range(len(eligible)):
    for j in range(i + 1, len(eligible)):
        first = eligible[i]
        second = eligible[j]
        if (second[2] > first[2] or
            (second[2] == first[2] and second[3] > first[3]) or
            (second[2] == first[2] and second[3] == first[3] and second[4] < first[4])):
            eligible[i], eligible[j] = eligible[j], eligible[i]
quota = 2
print("SCHOLARSHIP RESULTS")
for i in range(len(eligible)):
    student = eligible[i]
    roll, name, percentage, attendance, income = student
    if i < quota:
        status = "AWARDED"
    else:
        status = "WAITING LIST"
    print(roll, name, "Percentage:", round(percentage, 2),
          "Attendance:", attendance, "Income:", income, status)
if len(eligible) == 0:
    print("No eligible applicants")