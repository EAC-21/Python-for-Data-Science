#Assigment: Class 1 - Python Enric Aletà

#Ex1)
print("Hello, Python!")

#Ex2)
a = 7
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)

#Ex3)
name = "Enric"
print(f"Hello {name}!")

#Ex4)
Universities = ["UB","UPF","UAB","ESADE", "UIC"]
print(Universities)

    #print the first
print("First university:", Universities[0])
print("Last university:", Universities[-1])

#Ex5)
students = [
    {"name": "Enric", "age": 22, "degree": "BSc"},
    {"name": "Konstan", "age": 24, "degree": "MSc"},
    {"name": "Pepe", "age": 27, "degree": "PhD"}]

for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Degree: {student['degree']}")


#Ex6)
coordinates = [63,122]
print("Coordinates tuple:", coordinates)

print("X coordinate:", coordinates[0])
print("Y coordinate:", coordinates[1])

#Ex7)
colors = {"red","green", "blue"}
print(colors)

#Add other color
colors.add("yellow")
#Add repetitive color
colors.add("red")
#Check result adding yellow + trying to repit red
print(colors)  #NO es repetix el color vermell
#Remove color
colors.remove("red")
print(colors) 

light_colors = {"white", "green"}
merged_colors = colors.union(light_colors)

#Result of adding both lists
print(merged_colors)


#Ex8)
number = float(input("Tell me a number?"))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


#Ex9)
numbers = [1,2,3,4,5]
for number in numbers:
    print(number)

#Ex10)
number = 1
while number <= 5:
    print(number)
    number += 1  

#Ex11)
def grade_response(grade):
    match grade:
        case "A":
            return "Excellent!"
        case "B":
            return "Good job!"
        case "C":
            return "Fair."
        case "D":
            return "Needs improvement."
        case "F":
            return "Failing."
        case _:
            return "Invalid grade entered."

grade_input = input("Enter a grade (A, B, C, D, F): ")
response = grade_response(grade_input)
print(response)


#Ex12)
def greet(name):
    print(f"Hello, {name}!")

greet("Enric")

#Ex13)
def square(number):
    return number**2

print(square(4))
print(square(3))

#Ex14)
def multiply(a,b=1):
    return a*b

print(multiply(2,3))
print(multiply(11))

#Ex15)
numbers = list(range(1, 11))

squares = [number ** 2 for number in numbers]
squares

#Ex16)
students_grades = {
    "Enric": [5.5, 8.8, 7.8],
    "Pep": [9.2, 8.8, 3.4],
    "Jordi": [7.4, 8.2, 6.3]
}

def print_average_grades(students_grades):
    for student, grades in students_grades.items():
        average_grade = sum(grades) / len(grades)
        print(f"{student}: {average_grade:.2f}")

print_average_grades(students_grades)


#Ex17)
def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero!"
    else:
        return "Invalid operator!"

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

result = calculate(num1, num2, operator)
print(f"The result is: {result}")