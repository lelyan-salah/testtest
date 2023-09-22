import math

def sum(x=0, y=0):
    total = x + y
    return total

def subtract(x=0, y=0):
    total = x - y
    return total

def division(x=0, y=0):
    total = x / y
    return total

def multiply(x=0, y=0):
    total = x * y
    return total

def Calculatetrianglearea():
    base = int(input("Please enter the base: "))
    length = int(input("Please enter the length: "))
    area = 0.5 * base * length
    print("Triangle area =", area)

def Calculatecirclearea():
    radius = float(input("Please enter the radius: "))
    area = math.pi * (radius**2)
    print("Circle area =", area)

def Calculaterectanglearea():
    width = float(input("Please enter the width: "))
    length = float(input("Please enter the length: "))
    area = length * width
    print("Rectangle area =", area)

while True:
    print("\nMain Menu:")
    print("1. Sum")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Division")
    print("5. Calculate triangle area")
    print("6. Calculate circle area")
    print("7. Calculate rectangle area")
    print("8. Exit")

    choice = int(input("Enter the number of the operation you want: "))

    if choice == 1:
        num1 = float(input("Enter number1: "))
        num2 = float(input("Enter number2: "))
        result = sum(num1, num2)
        print("Sum =", result)
    elif choice == 2:
        num1 = float(input("Enter number1: "))
        num2 = float(input("Enter number2: "))
        result = subtract(num1, num2)
        print("Subtract =", result)
    elif choice == 3:
        num1 = float(input("Enter number1: "))
        num2 = float(input("Enter number2: "))
        result = multiply(num1, num2)
        print("Multiply =", result)
    elif choice == 4:
        num1 = float(input("Enter number1: "))
        num2 = float(input("Enter number2: "))
        result = division(num1, num2)
        print("Division =", result)
    elif choice == 5:
        Calculatetrianglearea()
    elif choice == 6:
        Calculatecirclearea()
    elif choice == 7:
        Calculaterectanglearea()
    elif choice == 8:
        print("Exit")
    else:
        print("its not valid")





