students = [
    ("IT201", "Asha", [72, 68, 81], 88, True),
    ("IT202", "Bharat", [65, 35, 74], 82, True),
    ("IT203", "Chitra", [80, 76, 69], 70, True),
    ("IT204", "Dev", [55, 62, 71], 80, False)
]
print("ACADEMIC PROGRESSION AUDIT")
for student in students:
    roll, name, marks, attendance, prerequisites = student
    reasons = []
    for index in range(len(marks)):
        if marks[index] < 40:
            reasons.append("Failed subject " + str(index + 1))
    if attendance < 75:
        reasons.append("Attendance below 75%")
    if not prerequisites:
        reasons.append("Prerequisite not completed")
    if len(reasons) == 0:
        print(roll, name, "ELIGIBLE FOR NEXT SEMESTER")
    else:
        print(roll, name, "NOT ELIGIBLE")
        for reason in reasons:
            print(" -", reason)
