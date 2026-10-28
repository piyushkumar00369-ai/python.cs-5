import math


def welcome():
    print("Welcome to the functions exercise!")


def add_numbers(first, second):
    return first + second


def circle_area(radius):
    return math.pi * radius * radius


def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"


def show_student(name, roll_number, course):
    print("Student name:", name)
    print("Roll number:", roll_number)
    print("Course:", course)


welcome()

first_number = float(input("Enter the first number to add: "))
second_number = float(input("Enter the second number to add: "))
print("Sum:", add_numbers(first_number, second_number))

radius = float(input("\nEnter the circle radius: "))
print("Circle area:", circle_area(radius))

number = int(input("\nEnter a number to check: "))
print(number, "is", even_or_odd(number))

student_name = input("\nEnter student name: ")
roll_number = input("Enter roll number: ")
course = input("Enter course: ")
show_student(student_name, roll_number, course)

print("\nFunction definition: writing a function using def.")
print("Function call: using the function's name to run its code.")