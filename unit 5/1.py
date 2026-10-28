# Open in write mode ("w") to create student.txt or replace its contents.
student_file = open("student.txt", "w", encoding="utf-8")
student_file.write("Name: Piyush\n")
student_file.write("Roll Number: 74\n")
student_file.write("Class: 2\n")
student_file.close()

# Open in read mode ("r") and display the saved student details.
# The with statement closes the file automatically when the block ends.
print("Student details:")
with open("student.txt", "r", encoding="utf-8") as student_file:
    print(student_file.read())