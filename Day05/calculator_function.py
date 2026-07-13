def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
print('==========')
print('Calculator')
print('==========')
a= int(input('Enter a number:'))
b= int(input('Enter another number:'))
addition= add(a,b)
print('Addition:', addition)
subtraction= subtract(a,b)
print('Subtraction:', subtraction)
multiplication = multiply(a,b)
print('Multiplication:', multiplication)
division = divide(a,b)
print('Division:', division)
