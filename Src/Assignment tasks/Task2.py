# Task2: Mathematical Operations

# Getting user inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform calculations
maximum = max(num1, num2)
power = num1 ** num2
subtraction = num1 - num2
multiplication = num1 * num2
addition = num1 + num2
division = num1 / num2 if num2 != 0 else "undefined (cannot be divide by zero)"

# Print results using f-string formatting
print(f"Maximum: {maximum}")
print(f"{num1} raised to the power of {num2}: {power}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Addition: {addition}")
print(f"Division: {division}")