import json

filename = "students.json"

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))

    students.append({
        "Name": name,
        "Marks": marks
    })

with open(filename, "w") as file:
    json.dump(students, file, indent=4)

print("Student records saved successfully!")

# Read and display the records
with open(filename, "r") as file:
    data = json.load(file)

print("\nStudent Records:")
for student in data:
    print("Name:", student["Name"], "| Marks:", student["Marks"])
