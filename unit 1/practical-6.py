# Input two strings
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# find string length

print("\n----String Length----")
print("Length of first string:", len(str1))

#convert uppercase and lowercase
print("\n----String Case Conversion----")
print("uppercase:", str1.upper())   
print("lowercase:", str2.lower())

# Acces characters using indexing
print("\n----String Indexing----")
print("First character :", str1[0])
print("Last character :", str2[-1])

# perform string slicing
print("\n----String Slicing----")
print("First three characters:", str1[:3])
print("Last three characters:", str2[-3:])

# concatenate two strings
print("\n----String Concatenation----")
print("Concatenation of both strings:", str1 + str2)