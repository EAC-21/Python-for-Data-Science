#Ex 1)
def fizzbuzz(n):
    for number in range(1, number +1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print("The number itself for other numbers")
fizzbuzz(20)  
print() 

#Ex 2)
list = (1, "Enric", 0.99, 333, "Pepe" , 3.223 )

integer_list = [x for x in list if isinstance(x, int)]
integer_list
print()

#Ex 3)
todo_list = []    #IMPORTANT: list sempre [] !!

def add_task(task):
    todo_list.append(task)
    
def show_tasks():
    for task in todo_list:
        print(task)

add_task("Finish homework")
add_task("Go to the gym")       

show_tasks()
print()

#Ex 4)
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temperatures_in_celsius = [22, 46, 51, 76]
converted_temperatures = [celsius_to_fahrenheit(temp) for temp in temperatures_in_celsius]

converted_temperatures
