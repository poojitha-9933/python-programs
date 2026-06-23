n = 4

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()


n = 4

for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()    


n = 4

for i in range(1, n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1))



n = 4

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
    


n = 4

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

n = 4

for i in range(1, n+1):
    for j in range(i):
        print(i, end=" ")
    print()



n = 4
num = 1

for i in range(1, n+1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
