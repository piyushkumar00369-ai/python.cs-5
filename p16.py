n = int(input("Enter N: "))
count = 1
sum_n = 0

while count <= n:
    sum_n += count
    count += 1

print("Sum of first", n, "natural numbers is", sum_n)
