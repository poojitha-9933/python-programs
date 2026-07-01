names = ["satoru", "suguru", "maki", "toji", "panda"]
search_name = input("Enter the name to search: ")
if search_name in names:
    print(search_name, "found in the list.")
else:
    print(search_name, "not found in the list.")
