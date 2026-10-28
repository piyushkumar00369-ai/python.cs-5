def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    return first / second


if __name__ == "__main__":
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))

    print("Addition:", add(first, second))
    print("Subtraction:", subtract(first, second))
    print("Multiplication:", multiply(first, second))
    print("Division:", divide(first, second))
