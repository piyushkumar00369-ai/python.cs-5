names = ["Nishit", "Vansh", "Disha", "Neel"]
name_set = set(names)
print("Set:", name_set)
print("Empty set:", set())

group1 = {"Nishit", "Vansh", "Disha"}
group2 = {"Vansh", "Neel"}

print("Union:", group1 | group2)
print("Intersection:", group1 & group2)
print("Difference:", group1 - group2)
print("Symmetric difference:", group1 ^ group2)

print("Group 1 is a subset of group 2:", group1.issubset(group2))
print("Is Nishit in group 1?", "Nishit" in group1)
