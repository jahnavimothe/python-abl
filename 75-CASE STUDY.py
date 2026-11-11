records = [
    ("IT101", "Asha", [88, 76, 91], 92, ("Python", "DBMS")),
    ("IT102", "Bharat", [65, 72, 80], 78, ("Python",)),
    ("IT101", "Chitra", [90, 85, 88], 89, ("Java",)),
    ("IT104", "", [75, 110, 68], 105, ())
]
seen = []
print("STUDENT RECORD VALIDATION")
for record in records:
    roll, name, marks, attendance, courses = record
    errors = []
    if roll in seen:
        errors.append("Duplicate roll number")
    else:
        seen.append(roll)
    if not roll.startswith("IT"):
        errors.append("Invalid roll number prefix")
    if name.strip() == "":
        errors.append("Name is missing")
    for mark in marks:
        if mark < 0 or mark > 100:
            errors.append("Marks outside 0-100")
            break
    if attendance < 0 or attendance > 100:
        errors.append("Attendance outside 0-100")
    if len(courses) == 0:
        errors.append("No course registered")
    if len(errors) == 0:
        print(roll, name, "VALID")
    else:
        print(roll, name, "INVALID")
        for error in errors:
            print(" -", error)
