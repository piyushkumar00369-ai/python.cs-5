numbers = []

for i in range(10):
    num = int(input("Enter a number {}: ".format(i + 1)))
    numbers.append(num)

    print("\n Maximum number is:", max(numbers))
    print("Minimum number is:", min(numbers))

    total = sum(numbers)
    average = total / len(numbers)

    print("Sum of numbers:", total)
    print("Average of numbers:", average)

    print("\n Even numbers are:")
    for num in numbers:
        if num % 2 == 0:
            print(num)

    print("\n Odd numbers are:")
    for num in numbers:
        if num % 2 != 0:
            print(num)