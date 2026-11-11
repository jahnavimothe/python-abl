requirements = [
    ("North", 55, 1),
    ("South", 40, 2),
    ("East", 35, 1),
    ("West", 20, 3)
]
for i in range(len(requirements)):
    for j in range(i + 1, len(requirements)):
        first = requirements[i]
        second = requirements[j]
        if second[2] < first[2] or (second[2] == first[2] and second[0] < first[0]):
            requirements[i], requirements[j] = requirements[j], requirements[i]
stock = 100
print("DISASTER RELIEF ALLOCATION")
total_unmet = 0
for area in requirements:
    name, demand, priority = area
    if demand < stock:
        allocated = demand
    else:
        allocated = stock
    unmet = demand - allocated
    stock = stock - allocated
    total_unmet = total_unmet + unmet
    print(name, "Priority:", priority, "Demand:", demand,
          "Allocated:", allocated, "Unmet:", unmet)
print("Remaining stock:", stock)
print("Total unmet demand:", total_unmet)