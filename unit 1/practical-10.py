numbers = []

for i in range(10):
    while True:
        try:
            num = int(input("Enter a number {}: ".format(i + 1)))
            break
        except ValueError:
            print("Please enter a valid integer.")
    numbers.append(num)

print("\nMaximum number is:", max(numbers))
print("Minimum number is:", min(numbers))

total = sum(numbers)
average = total / len(numbers)

print("Sum of numbers:", total)
print("Average of numbers:", average)

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

print("\nEven numbers are:")
if even_numbers:
    for num in even_numbers:
        print(num)
else:
    print("No even numbers")

print("\nOdd numbers are:")
if odd_numbers:
    for num in odd_numbers:
        print(num)
else:
    print("No odd numbers")