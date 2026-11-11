rooms = [("R101", 60), ("R102", 40), ("LAB1", 30)]
allocations = [
    ("Python", "LAB1", "Mon-9", "Dr Rao", 28),
    ("DBMS", "R101", "Mon-9", "Dr Sen", 55),
    ("Networks", "R101", "Mon-9", "Dr Rao", 45),
    ("Java", "R102", "Tue-10", "Dr Sen", 45)
]
errors_found = False
print("TIMETABLE VALIDATION")
for i in range(len(allocations)):
    course, room, period, teacher, students = allocations[i]
    errors = []
    capacity = 0
    for room_record in rooms:
        if room_record[0] == room:
            capacity = room_record[1]
    if capacity == 0:
        errors.append("Room does not exist")
    elif students > capacity:
        errors.append("Room capacity exceeded")
    for j in range(i):
        old = allocations[j]
        if old[1] == room and old[2] == period:
            errors.append("Room time clash")
        if old[3] == teacher and old[2] == period:
            errors.append("Instructor time clash")
    if len(errors) == 0:
        print(course, "VALID")
    else:
        errors_found = True
        print(course, "INVALID")
        for error in errors:
            print(" -", error)
if not errors_found:
    print("All allocations are valid")
