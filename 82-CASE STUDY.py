candidates = [
    ("P101", "Anu", 8.4, 82, 92),
    ("P102", "Bala", 7.2, 91, 85),
    ("P103", "Charan", 6.8, 95, 90),
    ("P104", "Diya", 8.8, 78, 88)
]
shortlist = []
for candidate in candidates:
    cid, name, cgpa, assessment, attendance = candidate
    if cgpa >= 7.0 and assessment >= 60 and attendance >= 80:
        academic_percent = cgpa * 10
        final_score = (academic_percent * 0.40 +
                       assessment * 0.50 + attendance * 0.10)
        shortlist.append((cid, name, final_score, assessment))
for i in range(len(shortlist)):
    for j in range(i + 1, len(shortlist)):
        first = shortlist[i]
        second = shortlist[j]
        if (second[2] > first[2] or
            (second[2] == first[2] and second[3] > first[3]) or
            (second[2] == first[2] and second[3] == first[3] and second[0] < first[0])):
            shortlist[i], shortlist[j] = shortlist[j], shortlist[i]
print("INTERNSHIP SHORTLIST")
if len(shortlist) == 0:
    print("No eligible candidates")
else:
    for i in range(len(shortlist)):
        candidate = shortlist[i]
        print(i + 1, candidate[0], candidate[1],
              "Final score:", round(candidate[2], 2),
              "Assessment:", candidate[3])