# Contact Book Application

contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter contact name: ")

        if name in contacts:
            print("Contact already exists!")
        else:
            phone = input("Enter phone number: ")
            contacts[name] = phone
            print("Contact added successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\nSaved Contacts:")
            print("------------------------")
            for name, phone in contacts.items():
                print(f"Name : {name}")
                print(f"Phone: {phone}")
                print("------------------------")

    elif choice == "3":
        name = input("Enter the contact name to update: ")

        if name in contacts:
            new_phone = input("Enter the new phone number: ")
            contacts[name] = new_phone
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter the contact name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Thank you for using the Contact Book!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
