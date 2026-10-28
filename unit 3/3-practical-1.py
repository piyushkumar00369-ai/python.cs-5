marks = []
for student in range(1, 11):
    mark = int(input(f"Enter marks for student {student}: "))
    marks.append(mark)

print("Student marks:", marks)

print("\nAccessing elements:")
print("First mark (positive index 0):", marks[0])
print("Last mark (negative index -1):", marks[-1])

print("\nMarks from index 2 to 5:", marks[2:6])

print("\nTraversing with a for loop:")
for mark in marks:
    print(mark)

print("\nTraversing with a while loop:")
index = 0
while index < len(marks):
    print(marks[index])
    index += 1

print("\nEach mark with its index:")
for index, mark in enumerate(marks):
    print(f"Index {index}: {mark}")