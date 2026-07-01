#Reverse a String
string = "Python"
print("Original String:", string)
print("Reversed String:", string[::-1])

#Check if a String is a Palindrome
string = "madam"

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

#Count Vowels in a String
string = "Hello World"
count = 0

for char in string.lower():
    if char in "aeiou":
        count += 1

print("Number of vowels:", count)

#Convert String to Uppercase and Lowercase
string = "Python Programming"

print("Uppercase:", string.upper())
print("Lowercase:", string.lower())

#Count Words in a String
string = "Python is easy to learn"

words = string.split()
print("Number of words:", len(words))

##Comprehension Programs##

#List Comprehension (Squares of Numbers)
numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print(squares)

#Dictionary Comprehension (Squares)
numbers = [1, 2, 3, 4, 5]

square_dict = {x: x * x for x in numbers}

print(square_dict)

#Set Comprehension (Unique Even Numbers)
numbers = [1, 2, 2, 3, 4, 4, 5, 6]

even_set = {x for x in numbers if x % 2 == 0}

print(even_set)
