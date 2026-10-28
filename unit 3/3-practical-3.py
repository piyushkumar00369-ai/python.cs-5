numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]
print("Squares:", squares)

even_numbers = [number for number in range(1, 11) if number % 2 == 0]
print("Even numbers:", even_numbers)

multiples_of_5 = [number for number in range(1, 21) if number % 5 == 0]
print("Multiples of 5:", multiples_of_5)

words = ["apple", "banana", "cherry"]
uppercase_words = [word.upper() for word in words]
print("Uppercase words:", uppercase_words)

marks = [35, 50, 80, 25]
passing_marks = [mark for mark in marks if mark >= 40]
print("Passing marks:", passing_marks)
