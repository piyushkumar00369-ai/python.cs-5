first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number

if second_number == 0:
    division = "Not defined (division by zero)"
    modulus = "Not defined (modulus by zero)"
    floor_division = "Not defined (division by zero)"
else:
    division = first_number / second_number
    modulus = first_number % second_number
    floor_division = first_number // second_number

exponentiation = first_number ** second_number

print("\nArithmetic Results")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus)
print("Floor Division:", floor_division)
print("Exponentiation:", exponentiation)