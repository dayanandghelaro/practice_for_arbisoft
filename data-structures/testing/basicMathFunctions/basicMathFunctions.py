def addition(a, b):
    if (type(a) not in [int, float]) or (type(b) not in [int, float]):
        raise TypeError("Only integer or float values can be added.")
    return a+b

def subtraction(a, b):
    if (type(a) not in [int, float]) or (type(b) not in [int, float]):
        raise TypeError("Only integer or float values can be subtracted.")
    return a-b

def multiplication(a, b):
    if (type(a) not in [int, float]) or (type(b) not in [int, float]):
        raise TypeError("Only integer or float values can be multiplied.")
    return a*b

def division(a, b):
    if (type(a) not in [int, float]) or (type(b) not in [int, float]):
        raise TypeError("Only integer or float values can be divided.")
    if b == 0 or b == 0.0:
        raise ZeroDivisionError("Can't divide by zero.")
    return a/b

def power(a, b):
    if (type(a) not in [int, float]) or (type(b) not in [int, float]):
        raise TypeError("Only integer or float values can be used for exponentiation.")
    return a**b


