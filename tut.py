import logging


logging.basicConfig(filename='app.log', level=logging.DEBUG)




def add (x, y):
    return x + y

def subtract (x, y):
    return x - y

def multiply (x, y):
    return x * y

def divide (x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
logging.debug(f"Addition Result: {add_result}")

subtract_result = subtract(num_1, num_2)
logging.debug(f"Subtraction Result: {subtract_result}")

multiply_result = multiply(num_1, num_2)
logging.debug(f"Multiplication Result: {multiply_result}")

divide_result = divide(num_1, num_2)
logging.debug(f"Division Result: {divide_result}")