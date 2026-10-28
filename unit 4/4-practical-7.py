import calendar
import datetime
import math
import os
import random
import statistics

number = int(input("Enter a non-negative integer: "))
print("Square root:", math.sqrt(number))
print("Power (number to the power of 2):", math.pow(number, 2))
print("Factorial:", math.factorial(number))

print("\nRandom number from 1 to 100:", random.randint(1, 100))

now = datetime.datetime.now()
print("\nCurrent date and time:", now)

year = int(input("\nEnter a year to display: "))
month = int(input("Enter a month (1-12): "))
print(calendar.month(year, month))

print("Current directory:", os.getcwd())
print("Directory contents:", os.listdir())

values = [
    float(value)
    for value in input("\nEnter numbers for statistics, separated by spaces: ").split()
]
if values:
    print("Mean:", statistics.mean(values))
    print("Median:", statistics.median(values))
    print("Mode:", statistics.mode(values))
else:
    print("No numbers were entered for statistics.")

student_id = f"{now:%Y%m%d}{random.randint(1000, 9999)}"
print("\nRandom student ID:", student_id)
print("ID generation date:", now.strftime("%Y-%m-%d"))