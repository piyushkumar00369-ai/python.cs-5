add = lambda a, b: a + b
square = lambda number: number ** 2
maximum = lambda a, b: a if a > b else b


def add_with_def(a, b):
    return a + b


numbers = [1, 2, 3, 4, 5]

print("Sum:", add(3, 4))
print("Square:", square(3))
print("Maximum:", maximum(3, 7))
print("Squares:", list(map(lambda number: number ** 2, numbers)))
print("Even numbers:", list(filter(lambda number: number % 2 == 0, numbers)))

students = [("Asha", 80), ("Disha", 95), ("Ravi", 70)]
print("Students by marks:", sorted(students, key=lambda student: student[1]))

print("Lambda addition:", add(3, 4))
print("def addition:", add_with_def(3, 4))
