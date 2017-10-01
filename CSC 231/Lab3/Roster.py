from Student import *

file = open("roster.txt", "r")

roster = []
for line in file:
    parts = line.split()
    lastName = parts[0]
    firstName = parts[1]
    gpa = float(parts[2])
    rost = Student(firstName, lastName, gpa)
    roster.append(rost)

for student in roster:
    print(student)

max = roster[0]
for student in roster:
    if student.gpa > max.gpa:
        max = student
print()
print("The highest GPA is: ", max)

# student1 = Student("Michelle", "Vernatter", 3.44)
# student2 = Student("Sydney", "Vernatter", 3.5)
#
# print(student1)
# print(student2)
