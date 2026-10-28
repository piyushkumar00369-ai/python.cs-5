students = ["Rahul", "Amit", "Priya", "Amit"]
print("Students:", students)

students.append("Rohan")
students.extend(["Neha", "Karan"])
students.insert(1, "Pooja")
print("After append, extend, and insert:", students)

print("Index of Priya:", students.index("Priya"))
print("Number of Amits:", students.count("Amit"))

students.remove("Amit")
print("After removing Amit:", students)

popped_student = students.pop()
print("Popped student:", popped_student)
print("After pop:", students)

students.sort()
print("Sorted:", students)

students.reverse()
print("Reversed:", students)

print("Is Rahul in the list?", "Rahul" in students)
print("Is Harsh not in the list?", "Harsh" not in students)

students.clear()
print("After clear:", students)