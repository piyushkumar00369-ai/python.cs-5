def square(number):
    return number * number


def calculate(first, second):
    return first + second, first - second, first * second, first / second


def marks_result(marks):
    total = sum(marks)
    return total, total / len(marks)


number = 5
print("Square:", square(number))

first, second = 10, 2
print("Maximum:", max(first, second))
print("Sum, difference, product, quotient:", calculate(first, second))

total, percentage = marks_result([80, 90, 70])
print("Total:", total)
print("Percentage:", percentage, "%")