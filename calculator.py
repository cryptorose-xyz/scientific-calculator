import math

# --- Basic Operations ---
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)

def factorial(n):
    if n < 0:
        raise ValueError("Cannot take factorial of a negative number")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def logarithm(a, base):
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers")
    if base <= 1:
        raise ValueError("Base must be greater than 1")
    return math.log(a, base)

def sine(a): return math.sin(a)
def cosine(a): return math.cos(a)
def tangent(a): return math.tan(a)

def cotangent(a):
    if math.tan(a) == 0:
        raise ValueError("Cotangent undefined")
    return 1 / math.tan(a)

def secant(a):
    if math.cos(a) == 0:
        raise ValueError("Secant undefined")
    return 1 / math.cos(a)

def cosecant(a):
    if math.sin(a) == 0:
        raise ValueError("Cosecant undefined")
    return 1 / math.sin(a)


# --- MAIN PROGRAM ---
print("Welcome to Roseline's Scientific Calculator 💻✨")

while True:
    print("\n--- Calculator ---")

    try:
        operation = input(
            "Choose operation (+, -, *, /, ^, sqrt, !, log, sin, cos, tan, cot, sec, csc, exit): "
        ).lower()

        if operation == "exit":
            print("Goodbye bitch 👋")
            break

        if operation == "sqrt":
            num = float(input("Enter number: "))
            print("Result:", square_root(num))

        elif operation == "!":
            num = int(input("Enter integer: "))
            print("Result:", factorial(num))

        elif operation == "log":
            num = float(input("Enter number: "))
            base = float(input("Enter base: "))
            print("Result:", logarithm(num, base))

        elif operation in ["sin", "cos", "tan", "cot", "sec", "csc"]:
            num = float(input("Enter angle (in radians): "))
            if operation == "sin":
                print("Result:", sine(num))
            elif operation == "cos":
                print("Result:", cosine(num))
            elif operation == "tan":
                print("Result:", tangent(num))
            elif operation == "cot":
                print("Result:", cotangent(num))
            elif operation == "sec":
                print("Result:", secant(num))
            elif operation == "csc":
                print("Result:", cosecant(num))

        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operation == "+":
                print("Result:", add(num1, num2))
            elif operation == "-":
                print("Result:", subtract(num1, num2))
            elif operation == "*":
                print("Result:", multiply(num1, num2))
            elif operation == "/":
                print("Result:", divide(num1, num2))
            elif operation == "^":
                print("Result:", power(num1, num2))
            else:
                print("Invalid operation")

    except ValueError as e:
        print("Error:", e)