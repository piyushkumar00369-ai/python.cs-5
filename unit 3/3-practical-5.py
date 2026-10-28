student = {"name": "Alice", "course": "Python", "marks": 85}
print("Student:", student)

print("Name:", student["name"])
print("Course:", student.get("course"))

student["email"] = "alice@example.com"
student["marks"] = 90
print("After adding email and updating marks:", student)

del student["course"]
student.pop("email")
print("After deleting course and email:", student)

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

student.update({"course": "Computer Science"})
student.setdefault("status", "Active")
print("After update and setdefault:", student)

student.clear()
print("After clear:", student)
