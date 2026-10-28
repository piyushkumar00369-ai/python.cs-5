name = input("Enter your name: ")
age = int(input("Enter your age: "))

student = (name, age, 85.5, True)
print("Tuple with different data types:", student)

empty_tuple = ()
single_item_tuple = (name,)
print("Empty tuple:", empty_tuple)
print("Single-item tuple:", single_item_tuple)

print("First item:", student[0])
print("Last item:", student[-1])
print("Tuple slice:", student[1:3])

print("Tuple items:")
for item in student:
    print(item)

try:
    student[0] = "New name"
except TypeError:
    print("Tuples cannot be changed after creation.")

student_list = [name, age, 85.5, True]
print("Tuple:", student)
print("List:", student_list)
student_list.append("Lists can be changed")
print("List after adding an item:", student_list)