while True:
    print("\nMenu")
    print("1. Add")
    print("2. Subtract")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Sum =", a + b)

        elif choice == 2:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Difference =", a - b)

        elif choice == 3:
            print("Program exited")
            break

        else:
            print("Invalid choice! Please select 1 to 3.")

    except ValueError:
        print("Error! Please enter numbers only.")
