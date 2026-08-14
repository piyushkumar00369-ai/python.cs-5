marks = int(input("Enter marks out of 100: "))
print("Your marks:", marks)

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "Failed"

print("Grade:", grade)

if grade == "Failed":
    print("You need to work harder.")
else:
    print("Excellent! Keep it up.")
