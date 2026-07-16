import json
import os

file_name = "inventory.json"

# Load data if file exists
if os.path.exists(file_name):
    with open(file_name, "r") as file:
        products = json.load(file)
else:
    products = {}

while True:

    print("\n===== Inventory Management System =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Search Product")
    print("6. Sell Product")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Add Product
    if choice == "1":

        name = input("Enter product name: ")

        if name in products:
            print("Product already exists!")

        else:
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))

            products[name] = {
                "Price": price,
                "Quantity": quantity
            }

            with open(file_name, "w") as file:
                json.dump(products, file, indent=4)

            print("Product added successfully!")

    # View Products
    elif choice == "2":

        if len(products) == 0:
            print("No products available.")

        else:
            print("\nProduct Details")
            for name in products:
                print("Product Name :", name)
                print("Price        :", products[name]["Price"])
                print("Quantity     :", products[name]["Quantity"])
                print("---------------------------")

    # Update Product
    elif choice == "3":

        name = input("Enter product name to update: ")

        if name in products:

            new_price = float(input("Enter new price: "))
            new_quantity = int(input("Enter new quantity: "))

            products[name]["Price"] = new_price
            products[name]["Quantity"] = new_quantity

            with open(file_name, "w") as file:
                json.dump(products, file, indent=4)

            print("Product updated successfully!")

        else:
            print("Product not found.")

    # Delete Product
    elif choice == "4":

        name = input("Enter product name to delete: ")

        if name in products:

            del products[name]

            with open(file_name, "w") as file:
                json.dump(products, file, indent=4)

            print("Product deleted successfully!")

        else:
            print("Product not found.")

    # Search Product
    elif choice == "5":

        name = input("Enter product name to search: ")

        if name in products:
            print("Product Found")
            print("Price :", products[name]["Price"])
            print("Quantity :", products[name]["Quantity"])

        else:
            print("Product not found.")

    # Sell Product
    elif choice == "6":

        name = input("Enter product name: ")

        if name in products:

            sell = int(input("Enter quantity to sell: "))

            if sell <= products[name]["Quantity"]:

                products[name]["Quantity"] = products[name]["Quantity"] - sell

                with open(file_name, "w") as file:
                    json.dump(products, file, indent=4)

                print("Product sold successfully!")
                print("Remaining Stock:", products[name]["Quantity"])

            else:
                print("Not enough stock.")

        else:
            print("Product not found.")

    # Exit
    elif choice == "7":

        print("Thank You!")
        break

    else:
        print("Invalid choice!")
