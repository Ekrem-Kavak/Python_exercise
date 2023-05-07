# Simple calculator for addition, subtraction, multiplication, division


print(""" Simple Calculator

[1] Addition
[2] Extraction
[3] Multiplication
[4] Divide 
[Q] Exit

""")

operation = input("Please, select the operation you want to do: ")

if operation == "1":
    number_1 = float(input("Please, enter a first number: "))
    number_2 = float(input("Please, enter a number second number: "))
    add = number_1 + number_2
    print(f"Result of the operation: {add}")

elif operation == "2":
    number_1 = float(input("Please, enter a first number: "))
    number_2 = float(input("Please, second a first number: "))
    ext = number_1 - number_2
    print(f"Result of the operation: {ext}")

elif operation == "3":
    number_1 = float(input("Please, enter a first number: "))
    number_2 = float(input("Please, second a first number: "))
    mult = number_1 * number_2
    print(f"Result of the operation: {mult}")

elif operation == "4":
    number_1 = float(input("Please, enter a first number: "))
    number_2 = float(input("Please, second a first number: "))
    div = number_1 / number_2
    print(f"Result of the operation: {div}")
    
elif operation == "Q" or operation == "q":
    print("exit")

