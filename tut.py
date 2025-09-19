import logging
import example

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler("app.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)







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

num_1 = 11
num_2 = 8

add_result = add(num_1, num_2)
logger.debug(f"Addition Result: {add_result}")

subtract_result = subtract(num_1, num_2)
logger.debug(f"Subtraction Result: {subtract_result}")

multiply_result = multiply(num_1, num_2)
logger.debug(f"Multiplication Result: {multiply_result}")

divide_result = divide(num_1, num_2)
logger.debug(f"Division Result: {divide_result}")