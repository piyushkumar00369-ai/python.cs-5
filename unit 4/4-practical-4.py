count = 0


def show_scope():
    message = "This is a local variable."
    print(message)
    print("Global count:", count)


def increase_count():
    global count
    count += 1


def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number - 1)


def sum_natural(number):
    if number == 0:
        return 0
    return number + sum_natural(number - 1)


def fibonacci(count, first=0, second=1):
    if count == 0:
        return
    print(first, end=" ")
    fibonacci(count - 1, second, first + second)


show_scope()
increase_count()
print("Count after increase:", count)

print("Factorial of 5:", factorial(5))
print("Sum from 1 to 5:", sum_natural(5))
print("Fibonacci numbers:")
fibonacci(7)
print()

print("Base conditions stop recursion from continuing forever.")
