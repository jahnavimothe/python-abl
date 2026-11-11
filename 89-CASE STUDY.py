rooms = [
    ["B101", "Boys", 2, []],
    ["B102", "Boys", 1, []],
    ["G101", "Girls", 2, []]
]
students = [
    ("S101", "Asha", "Girls"),
    ("S102", "Bala", "Boys"),
    ("S103", "Chitra", "Girls"),
    ("S104", "Dev", "Boys"),
    ("S105", "Esha", "Girls"),
    ("S106", "Farhan", "Boys"),
    ("S107", "Gopal", "Boys")
]
unallocated = []
assigned_ids = []
for student in students:
    sid, name, category = student
    placed = False
    if sid in assigned_ids:
        unallocated.append((sid, name, "Duplicate student record"))
    else:
        for room in rooms:
            room_id, room_category, capacity, occupants = room
            if room_category == category and len(occupants) < capacity:
                occupants.append((sid, name))
                assigned_ids.append(sid)
                placed = True
                break
        if not placed:
            unallocated.append((sid, name, "No suitable room available"))
print("HOSTEL ALLOCATION")
for room in rooms:
    print(room[0], room[1], "Occupants:", len(room[3]), "/", room[2])
    for occupant in room[3]:
        print(" -", occupant[0], occupant[1])
print("\nUNALLOCATED STUDENTS")
for student in unallocated:
    print(student[0], student[1], student[2])
print("Total unallocated:", len(unallocated))
