teams = [
    ("CodeStars", ["Asha", "Ravi", "Neha"], [80, 90, 95]),
    ("ByteForce", ["Kiran", "Maya"], [88, 86, 91]),
    ("SoloCoder", ["Arun"], [99, 99, 99]),
    ("Debuggers", ["Ira", "Dev", "Sam", "Tia", "Raj"], [90, 90, 90]),
    ("LoopLegends", ["Nikhil", "Pia"], [92, 90, 90])
]
valid = []
print("TEAM VALIDATION")
for team in teams:
    name, members, scores = team
    if 2 <= len(members) <= 4:
        total = sum(scores)
        valid.append((name, len(members), total, scores[2]))
        print(name, "Valid team")
    else:
        print(name, "Invalid team size:", len(members))
for i in range(len(valid)):
    for j in range(i + 1, len(valid)):
        first = valid[i]
        second = valid[j]
        if (second[2] > first[2] or
            (second[2] == first[2] and second[3] > first[3]) or
            (second[2] == first[2] and second[3] == first[3] and second[0] < first[0])):
            valid[i], valid[j] = valid[j], valid[i]
print("\\nHACKATHON RANKING")
for i in range(len(valid)):
    team = valid[i]
    print(i + 1, team[0], "Members:", team[1],
          "Total:", team[2], "Round 3:", team[3])