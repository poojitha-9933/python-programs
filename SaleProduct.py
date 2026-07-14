products = {}

while True:
    print("\n1. Add Product")
    print("2. View Products")
    print("3. Sale Product")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter product name: ")

        if name in products:
            print("Product already exists! Duplicate product names are not allowed.")
        else:
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))

            products[name] = {
                "Price": price,
                "Quantity": quantity
            }

            print("Product added successfully!")

    elif choice == "2":
        if not products:
            print("No products available.")
        else:
            print("\nProduct List:")
            for name, details in products.items():
                print(f"Name: {name}")
                print(f"Price: {details['Price']}")
                print(f"Quantity: {details['Quantity']}")
                print("-" * 20)

    elif choice == "3":
        name = input("Enter product name to sell: ")

        if name in products:
            sale_qty = int(input("Enter quantity sold: "))

            if sale_qty <= products[name]["Quantity"]:
                products[name]["Quantity"] -= sale_qty
                print("Sale completed successfully!")
                print("Current stock:", products[name]["Quantity"])
            else:
                print("Insufficient stock!")
                print("Current stock:", products[name]["Quantity"])
        else:
            print("Product not found!")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please try again.")
