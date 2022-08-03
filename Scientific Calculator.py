import math


# operations in scientific calculator
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def sqrt(a):
    r = math.sqrt(a)
    return r


def exp(a):
    return a ** 2


def sin(x):
    return math.sin(x)


def cos(x):
    return math.cos(x)


def tan(x):
    return math.tan(x)


# choosing the operation
print('''choose a number for the fallowing operations:
1- Addition(x,y)
2- Subtraction(x,y)
3- Multiplication(x,y)
4- Divide(x,y)
5- Square(x)
6- Square root (x)
7- sin(x)
8- cos(x)
9- tan(x)''')

op = int(input(' what operation do you want input?:'))

# calculator script
while op < 10:
    if op == 1:
        x = int(input('enter x'))
        y = int(input('enter y'))
        z = add(x, y)
        print('Addition:', z)
    elif op == 2:
        x = int(input('enter x'))
        y = int(input('enter y'))
        z = subtract(x, y)
        print('Subtraction:', z)
    elif op == 3:
        x = int(input('enter x'))
        y = int(input('enter y'))
        z = multiply(x, y)
        print('Multiplication:', z)

    elif op == 4:
        x = int(input('enter x'))
        y = int(input('enter y'))
        z = divide(x, y)
        print('Divide:', z)

    elif op == 5:
        x = int(input('enter x'))
        z = exp(x)
        print('Square:', z)

    elif op == 6:
        x = int(input('enter x'))
        z = sqrt(x)
        print('Square root:', z)

    elif op == 7:
        x = int(input('enter x'))
        z = sin(x)
        print('sin(x):', z)

    elif op == 8:
        x = int(input('enter x'))
        z = co(x)
        print('cos(x):', z)

    elif op == 9:
        x = int(input('enter x'))
        z = tan(x)
        print('tan(x):', z)

    else:
        print('choose another operation')

    new = int(input(' do you want to continue? (Yes - 1) (No - 0)'))
    if new == 1:
        op = int(input('enter operation:'))
    elif new == 0:
        print('Thanks for using the scientific calculator')
        break
