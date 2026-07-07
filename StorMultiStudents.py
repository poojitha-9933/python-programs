students = [
    ("Poojitha", 90),
    ("Rahul", 85),
    ("Sneha", 95)
]

file = open("students.txt", "w")

for name, marks in students:
    file.write(name + "," + str(marks) + "\n")

file.close()

file = open("students.txt", "r")

print("Student Records:")
for line in file:
    name, marks = line.strip().split(",")
    print("Name:", name, "Marks:", marks)

file.close()
