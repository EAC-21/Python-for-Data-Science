#PDS_Session1)

#Ex3
name = "Enric"
print(f"My name is {name}")   #IMPORTNAT: {} !!
print()


#Ex5 Dictionaires      #IMPORTANT !!
student = {
    "name": "Enric",
    "age": 21,
    "grade": "A"
}

# Printing each key-value pair in the dictionary
for key, value in student.items():
    print(f"{key}: {value}")
print()


#Ex6 Tuples
# Defining a tuple called coordinates
coordinates = (5, 10)

# Printing the entire tuple
print("Coordinates:", coordinates)

# Accessing and printing each element by its index
print("X-coordinate:", coordinates[0])
print("Y-coordinate:", coordinates[1])
print()


#Ex8 Conditional Statements
number_told = int(input("Tell me a number:"))

if number_told > 0:
    print("The number told is positive")
elif number_told <0:
    print("The number told is negative")
else:
    print("The number told is equal to 0")
print()


#Ex9 For Loop
for number in range(1,6):
    print(number)
print()


#Ex10 While Loop           #IMPORTANT: !!!
number = 1

while number <= 5:  
    print(number)  
    number += 1     #IMPORTANT: Increment the number to aviod infinit loops
print()


#Ex 11 Match Satatement    #IMPORTANT:Revisar
def grade_message(grade):
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

message = grade_message(grade_input)
print(message)
print()


#Ex 12 Function
def greet(name):
    print(f"Hello, {name}!")

greet("Enric") 
print()


#Ex 13 Function with Return Value
def square (number):
    return number**2     #IMPORTANT: al quadrat es **

print(square(5))
print()


#Ex14  Function with Default Parameters
def multiply (a,b):   #Set default b=1 --> def multiply (a,b=1)
    return a*b

print(multiply(3,4))
print()

#Ex15 List Comprehension
numbers = list(range(1,11))    #IMPORTANT: No loops...

squares = [number **2 for number in numbers]
print(squares)
print()


#Ex16 Nested Data Strucutre           #IMPORTANT repasar
students_grades = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 84],
    "Charlie": [75, 80, 72]
}

def print_average_grades(students_grades):
    for student, grades in students_grades.items():
        average_grade = sum(grades) / len(grades)
        print(f"{student}: {average_grade:.2f}")

print_average_grades(students_grades)
print()

#Ex 17 Simple Calculator
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

