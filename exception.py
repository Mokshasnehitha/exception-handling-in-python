try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("Result is:", result)

except ZeroDivisionError:
    print("Error: you cannot divide by zero")

except ValueError:
    print("Error: Invalid input, please enter an integer")

print("Program continues")


try:
    x = int(input("Enter number: "))
    y = 10 / x
    print("Result:", y)

except ZeroDivisionError:
    print("Error: Division by zero")

except ValueError:
    print("Error: Invalid input")


try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Oops! Invalid input")
else:
    print("You entered:", num)


try:
    file = open("data.txt", "r")
    read_data = file.read()
    print(read_data)

except FileNotFoundError:
    print("File not found")

finally:
    print("Execution completed")
    
age = int(input("Enter age: ")          )
if age < 18:
    raise Exception("Age must be atleast 18! ")


