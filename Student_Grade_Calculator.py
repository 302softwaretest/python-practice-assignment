student = input("Enter student name: ")

math = float(input("Enter Math grade: "))
biology = float(input("Enter Biology grade: "))
physics = float(input("Enter Physics grade: "))

total = math + biology + physics
average = total / 3

if average >= 80:
    grade = "A+"
elif average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"

print(f"\nStudent Name: {student}")
print(f"Total Marks: {total}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")