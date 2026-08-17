a = [int(input("Enter first value for a: ")), 
     int(input("Enter second value for a: ")), 
     int(input("Enter third value for a: "))]
b = [int(input("Enter first value for b: ")), 
     int(input("Enter second value for b: ")), 
     int(input("Enter third value for b: "))]
c = a

# Using is
print("\na is b:", a is b)
print("a is c:", a is c)

# Using is not
print("\na is not b:", a is not b)
print("a is not c:", a is not c)