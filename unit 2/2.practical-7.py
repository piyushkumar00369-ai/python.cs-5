numbers = []
for i in range(4):
    numbers.append(int(input(f"Enter number {i + 1}: ")))
check_number = int(input("Enter a number to check in the list: "))
print(check_number, "in numbers:", check_number in numbers)
print(check_number, "not in numbers:", check_number not in numbers)

# Tuple
colors = []
for i in range(3):
    colors.append(input(f"Enter color {i + 1}: "))
colors = tuple(colors)
check_color = input("Enter a color to check in the tuple: ")
print("'" + check_color + "' in colors:", check_color in colors)
print("'" + check_color + "' not in colors:", check_color not in colors)

# String
name = input("Enter a word: ")
check_char = input("Enter a character to check in the string: ")
print("'" + check_char + "' in name:", check_char in name)
print("'" + check_char + "' not in name:", check_char not in name)