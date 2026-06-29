numbers = []

n = int(input("Enter the number of elements: "))

print("Enter the elements:")
for i in range(n):
    numbers.append(int(input()))
numbers.sort()

print("Sorted List:", numbers)

key = int(input("Enter the element to search: "))

if key in numbers:
    print("Element found at index:", numbers.index(key))
else:
    print("Element not found.")
