# Accept 5 numbers from the user and store them in a list
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Display maximum and minimum values
print("Original list:", numbers)
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))

# Modify one element
index = int(input("Enter the index (0 to 4) of the element to modify: "))
new_value = int(input("Enter the new value: "))
numbers[index] = new_value

# Print the updated list
print("Updated list:", numbers)