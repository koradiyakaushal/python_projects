import sympy

fx = input("Enter function fx: ")
n = int(input("enter limit x to: "))
print(sympy.limit(fx, 'x', n))

# using sumpy library
# https://www.sympy.org/en/index.html
