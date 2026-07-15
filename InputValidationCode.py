import json
import os

file_name = "students.json"
if os.path.exists(file_name):
    file = open(file_name, "r")
    students = json.load(file)
    file.close()
    print("Previous data loaded.")
else:
    students = []
while True:
    try:
        n = int(input("Enter number of students: "))
        break
    except ValueError:
        print("Please enter numbers only!")
for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter Name: ")

    while True:
        try:
            marks = float(input("Enter Marks: "))
            break
        except ValueError:
            print("Please enter valid marks!")

    students.append({
        "Name": name,
        "Marks": marks
    })
file = open(file_name, "w")
json.dump(students, file, indent=4)
file.close()

print("\nData saved successfully!")

file = open(file_name, "r")
data = json.load(file)
file.close()

print("\nStudent Records")
for student in data:
    print("Name:", student["Name"])
    print("Marks:", student["Marks"])
