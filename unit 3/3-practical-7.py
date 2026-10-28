numbers = [1, 2, 3, 3]
print("List:", numbers)
print("Tuple:", tuple(numbers))
print("Dictionary:", {number: "Student" for number in numbers})

numbers_set = set(numbers)
print("Set:", numbers_set)

numbers_set.add(4)
numbers_set.update([5, 6])
print("After add and update:", numbers_set)

numbers_set.remove(2)
numbers_set.discard(10)
print("After remove and discard:", numbers_set)

print("Removed by pop:", numbers_set.pop())
print("After pop:", numbers_set)

other_set = {3, 4, 7}
print("Union:", numbers_set | other_set)
print("Intersection:", numbers_set & other_set)
print("Difference:", numbers_set - other_set)

numbers_set.clear()
print("After clear:", numbers_set)
