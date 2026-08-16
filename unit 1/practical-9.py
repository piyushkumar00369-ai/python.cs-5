numbers = [12, 5, 18, 7, 20, 3]

# Conditional statement using list
if numbers:
    print("The list is not empty.")
else:
    print("The list is empty.")

# Check whether a value exists in the list
if 18 in numbers:
    print("\n18 is present in the list.")
else:
    print("18 is not present in the list.")

# Loop through the list
print("\nNumbers in the list:")
for num in numbers:
    print(num)

# Conditional statements inside a loop
print("\nEven and odd numbers:")
for num in numbers:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")