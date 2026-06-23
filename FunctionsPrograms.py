def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

num = int(input("Enter number: "))
print("Factorial =", factorial(num))


def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

text = input("Enter string: ")

if palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")



def area_circle(r):
    return 3.14 * r * r

radius = float(input("Enter radius: "))
print("Area =", area_circle(radius))



def simple_interest(p, r, t):
    return (p * r * t) / 100

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

print("Simple Interest =", simple_interest(p, r, t))




def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter number: "))
print(check_even_odd(num))
