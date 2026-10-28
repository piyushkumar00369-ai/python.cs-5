# Make a file so there is something to read.
with open("student.txt", "w", encoding="utf-8") as student_file:
    student_file.write("Name: Piyush\n")
    student_file.write("Roll Number: 74\n")

# r means read. read() gets all the text.
with open("student.txt", "r", encoding="utf-8") as student_file:
    print("read() - the whole file:")
    print(student_file.read())


# readline() gets one line.
with open("student.txt", "r", encoding="utf-8") as student_file:
    print("readline() - one line:")
    print(student_file.readline(), end="")

# readlines() gets all lines in a list.
with open("student.txt", "r", encoding="utf-8") as student_file:
    print("readlines() - all lines as a list:")
    print(student_file.readlines())

# w means write. It replaces the old contents.
with open("student.txt", "w", encoding="utf-8") as student_file:
    student_file.write("Name: Piyush\n")
    student_file.write("Roll Number: 74\n")
    student_file.write("Class: 2\n")

with open("student.txt", "r", encoding="utf-8") as student_file:
    print("After w, the old contents are replaced:")
    print(student_file.read())

# a means add new text at the end without removing old text.
with open("student.txt", "a", encoding="utf-8") as student_file:
    student_file.write("Grade: A\n")

with open("student.txt", "r", encoding="utf-8") as student_file:
    print("After a, the new record is added:")
    print(student_file.read())

# x creates a new file. It gives an error if the file already exists.
try:
    with open("student-exclusive.txt", "x", encoding="utf-8") as student_file:
        student_file.write("Created with exclusive mode.\n")
    print("x: created student-exclusive.txt")
except FileExistsError:
    print("FileExistsError: student-exclusive.txt already exists.")

# r gives an error if the file does not exist.
try:
    with open("missing-student.txt", "r", encoding="utf-8") as student_file:
        print(student_file.read())
except FileNotFoundError:
    print("FileNotFoundError: missing-student.txt was not found.")

# wb writes bytes; rb reads bytes.
binary_data = bytes([0, 1, 2, 255])
with open("student-data.bin", "wb") as binary_file:
    binary_file.write(binary_data)

with open("student-data.bin", "rb") as binary_file:
    print("rb: binary data:", binary_file.read())