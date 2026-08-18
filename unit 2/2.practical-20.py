print("=" * 20)
print("MULTIPLICATION TABLES FROM 1 TO 10")
print("=" * 20)

start = 1
end = 10
limit = 10

print()

for num in range(start, end + 1):

    print()
    print("*" * 10)
    print("Multiplication Table of", num)
    print("*" * 10)

    for i in range(1, limit + 1):

        result = num * i

        print(num, "x", i, "=", result)

    print("*" * 10)
    print("Table of", num, "completed.")
    print("*" * 10)

print()