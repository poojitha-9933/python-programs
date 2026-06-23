score = 0
attempt = 0

while attempt < 3:
    print("\nAttempt:", attempt + 1)

    n = int(input("Enter rows: "))

    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()

    score += 10
    attempt += 1

    print("Score:", score)

print("\nFinal Score:", score)
print("Total Attempts:", attempt)
