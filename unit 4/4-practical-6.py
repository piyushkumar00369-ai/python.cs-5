import calculator
from calculator import add, subtract, multiply, divide as divide_numbers


def main():
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))

    print("\nUsing the complete calculator module:")
    print("Addition:", calculator.add(first, second))
    print("Subtraction:", calculator.subtract(first, second))
    print("Multiplication:", calculator.multiply(first, second))
    print("Division:", calculator.divide(first, second))

    print("\nUsing individually imported functions:")
    print("Addition:", add(first, second))
    print("Subtraction:", subtract(first, second))
    print("Multiplication:", multiply(first, second))
    print("Division using the alias divide_numbers:", divide_numbers(first, second))


if __name__ == "__main__":
    main()