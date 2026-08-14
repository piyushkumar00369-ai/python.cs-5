limit = int(input("Enter the value where the loop should stop: "))

for i in range(1, limit + 1):
    if i == limit:
        print(i)
        break
    print(i)
