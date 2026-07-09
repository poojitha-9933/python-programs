filename = "students.txt"

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")

        while True:
            marks = input("Enter marks: ")

            if not marks.isdigit():
                print("Error: Please enter numbers only.")
            else:
                marks = int(marks)
                if 0 <= marks <= 100:
                    break
                else:
                    print("Error: Marks should be between 0 and 100.")

        file = open(filename, "a")
        file.write(name + "," + str(marks) + "\n")
        file.close()
        print("Student added successfully.")

    elif choice == "2":
        try:
            file = open(filename, "r")
            print("\nStudent Records:")
            for line in file:
                name, marks = line.strip().split(",")
                print("Name:", name, "Marks:", marks)
            file.close()
        except FileNotFoundError:
            print("Error: Student file not found.")

    elif choice == "3":
        print("Program exited.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
