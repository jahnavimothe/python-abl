students = [
    ("IT101", "Asha", 22000, 88, 72),
    ("IT102", "Bharat", 18000, 82, 65),
    ("IT103", "Chitra", 21000, 68, 55),
    ("IT104", "Deepak", 25000, 80, 32)
]
print("EXAMINATION ELIGIBILITY AUDIT")
for student in students:
    roll, name, fee_paid, attendance, internal = student
    reasons = []
    if fee_paid < 20000:
        reasons.append("Fee pending")
    if attendance < 75:
        reasons.append("Attendance below 75%")
    if internal < 40:
        reasons.append("Internal marks below 40")
    if len(reasons) == 0:
        print(roll, name, "ELIGIBLE")
    else:
        print(roll, name, "NOT ELIGIBLE")
        for reason in reasons:
            print(" -", reason)
