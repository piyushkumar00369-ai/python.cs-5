num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Choose operation: +, -, *, /")
op = input("Enter operation: ")

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", num1 / num2)
else:
    print("Invalid operation")
