







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

subtract_result = subtract(num_1, num_2)

multiply_result = multiply(num_1, num_2)

divide_result = divide(num_1, num_2)