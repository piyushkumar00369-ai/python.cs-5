first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))

if first >= second:
    if first >= third:
        print("First number is the largest")
    else:
        print("Third number is the largest")
else:
    if second >= third:
        print("Second number is the largest")
    else:
        print("Third number is the largest")
