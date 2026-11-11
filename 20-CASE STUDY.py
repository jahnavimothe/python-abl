candidates = [
    ("C104", "Ravi", 86, 91, 84),
    ("C102", "Meena", 92, 88, 90),
    ("C103", "Kiran", 78, 95, 88),
    ("C101", "Sara", 90, 91, 89)
]
eligible = []
for candidate in candidates:
    app_id, name, maths, physics, chemistry = candidate
    aggregate = (maths + physics + chemistry) / 3
    if maths >= 75 and physics >= 70 and aggregate >= 80:
        eligible.append((app_id, name, aggregate, maths))
for i in range(len(eligible)):
    for j in range(i + 1, len(eligible)):
        first = eligible[i]
        second = eligible[j]
        if (second[2] > first[2] or
            (second[2] == first[2] and second[3] > first[3]) or
            (second[2] == first[2] and second[3] == first[3] and second[0] < first[0])):
            eligible[i], eligible[j] = eligible[j], eligible[i]
print("ADMISSION MERIT LIST")
if len(eligible) == 0:
    print("No candidate qualified")
else:
    for i in range(len(eligible)):
        candidate = eligible[i]
        print(i + 1, candidate[0], candidate[1],
              "Aggregate:", round(candidate[2], 2),
              "Maths:", candidate[3], "SELECTED")