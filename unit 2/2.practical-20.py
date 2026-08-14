num = int(input("Enter a number to print its multiplication table: "))
limit = int(input("How many multiples do you want to print? "))

print("Table of", num)
for i in range(1, limit + 1):
    print(num, "x", i, "=", num * i)

