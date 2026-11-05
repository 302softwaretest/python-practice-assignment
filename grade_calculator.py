Student = input("Enter the student name: ")
Math = float(input("Enter the math number: "))
English = float(input("Enter the English number: "))
Python = float(input("Enter the Python number: "))
Avarage = (Math + English + Python) / 3

if Avarage >= 80:
    Grade = "A+"
elif Avarage >= 70:
    Grade = "A"
elif Avarage >= 60:
    Grade = "A-"
elif Avarage >= 50:
    Grade = "B"
elif Avarage >= 40:
    Grade = "C"
else:
    Grade = "F"

print (f"Student's Name: {Student}")

print (f"Average = {Avarage}")
print (f"Final Grde = {Grade}")
