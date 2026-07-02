

def addition(a, b):
    return a+b;

def subtraction(a,b):
    return a-b;

def multiplication(a, b):
    return a*b;

def division(a, b):
    if(b == 0):
        return "Runtime Error"
    else:
        return a/b;

def checker(a):
    if(a % 2 == 0):
        return "you entered even number"
    else:
        return "you entered odd number"