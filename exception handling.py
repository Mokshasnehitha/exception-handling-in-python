def get_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Try again!")

num1 = get_number("Enter first number: ")
num2 = get_number("Enter second number: ")

try:
    res = num1 / num2

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Division Result:", res)

finally:
    print("Execution done. Thanks!")