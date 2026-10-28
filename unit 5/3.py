"""Write, read, and search a student-record file."""

import os

records_file = "student-records.txt"
students = [
    "Panchal Disha, 82, Class 2",
    "Panchal Nishit, 66, Class 2",
    "Patal Vansh, 28, Class 1",
]

# Write the student records. This replaces the file each time.
with open(records_file, "w", encoding="utf-8") as file:
    for student in students:
        file.write(student + "\n")

# Add one more record without replacing the existing ones.
with open(records_file, "a", encoding="utf-8") as file:
    file.write("Noah Kim, 104, Class 11\n")

# Read and display all records.
print("Student records:")
with open(records_file, "r", encoding="utf-8") as file:
    contents = file.read()
    print(contents, end="")

# Search for a student by name.
search_name = "Panchal Disha"
if search_name.casefold() in contents.casefold():
    print(f"\nFound: {search_name}")
else:
    print(f"Not found: {search_name}")

print(f"\nFile exists: {os.path.exists(records_file)}")