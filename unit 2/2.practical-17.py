num = int(input("Enter a number: "))

print("\nMultiplication Table of", num)
print("--------------------------")

i = 1

for i in range(1, 11):
    result = num * i
    print(num, "x", i, "=", result)

print("--------------------------")
print("Multiplication table completed successfully!")
