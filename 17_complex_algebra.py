c1 = complex(input("first complex: "))
c2 = complex(input("second complex: "))
# c1 = 10+5j
# c2 = 5+4j


def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


def negation(x):
    return -x


def inversion(x):
    a = x.real
    b = x.imag
    return complex(a, -b) / (1 / a ** 2 + b ** 2)


# print(addition(c1, c2))
# print(subtraction(c1, c2))
# print(multiplication(c1, c2))
# print(division(c1, c2))
# print(negation(c1))
# print(inversion(c1))
