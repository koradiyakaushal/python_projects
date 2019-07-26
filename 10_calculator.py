import math


def ask_number(s):
    return float(input(s))


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Log")
print("6.sin")
print("7.cos")
print("8.tan")
print("9.factorial")
print("10.x**y")

while True:

    choice = input("enter choice(1/2/3/4/5/6/7/8/9/10): ")

    if choice == "1":
        print("addition")
        n1 = ask_number(r"enter first number: ")
        n2 = ask_number(r"enter second number: ")
        print("addition of {} and {} is {}".format(n1, n2, n1 + n2))
    elif choice == "2":
        print("subtraction")
        n1 = ask_number(r"enter first number: ")
        n2 = ask_number(r"enter second number: ")
        print("subtraction of {} and {} is {}".format(n1, n2, n1 - n2))
    elif choice == "3":
        print("multiplication")
        n1 = ask_number(r"enter first number: ")
        n2 = ask_number(r"enter second number: ")
        print("multiplication of {} and {} is {}".format(n1, n2, n1 * n2))
    elif choice == "4":
        print("division")
        n1 = ask_number(r"enter first number: ")
        n2 = ask_number(r"enter second number: ")
        print("division of {} and {} is {}".format(n1, n2, n1 / n2))
    elif choice == "5":
        n1 = ask_number(r"enter log number: ")
        n2 = ask_number(r"enter base: ")
        print("log of {} with base {} is {}".format(n1, n2, math.log(n1, 10)))
    elif choice == "6":
        n1 = ask_number(r"enter sin: ")
        print("sin({}) is {}".format(n1, math.sin(n1)))
    elif choice == "7":
        n1 = ask_number(r"enter cos: ")
        print("cos({}) is {}".format(n1, math.cos(n1)))
    elif choice == "8":
        n1 = ask_number(r"enter tan: ")
        print("tan({}) is {}".format(n1, math.tan(n1)))
    elif choice == "9":
        n1 = ask_number(r"enter factorial number: ")
        print("factorial of {} is {}".format(n1, factorial(n1)))
    elif choice == "10":
        n1 = ask_number(r"enter number: ")
        n2 = ask_number(r"enter power of number : ")
        print("{} ** {} = {}".format(n1, n2, n1 ** n2))
    else:
        print("invalid choice.")
        break

# def addition(x, y):
#     return x + y
#
#
# def subtraction(x, y):
#     return x - y
#
#
# def multiplication(x, y):
#     return x * y
#
#
# def division(x, y):
#     return x / y
#
# while True:
#     n = input("enter command: ")
#     n1 = float(input("enter number: "))
#     n2 = float(input("enter number: "))
#     try:
#         if n == '+':
#             print("sum is: ", (n1 + n2))
#         elif n == '-':
#             print("division is: ", (n1 - n2))
#         elif n == '*':
#             print("multiplication is: ", (n1 * n2))
#         elif n == '/':
#             print("division is: ", (n1 / n2))
#         elif n == 'sin':
#             print("sin({}) = {}".format(n1, math.sin(n1)))
#         elif n == 'cos':
#             print("cos({}) = {}".format(n1, math.cos(n1)))
#         elif n == 'tan':
#             print("tan({}) = {}".format(n1, math.tan(n1)))
#         elif n == 'log':
#             print("log({}) = {}".format(n1, math.log(n1)))
#         else:
#             print("command not found. ")
#             break
#     except:
#         print("enter valid values. ")
# # ans = 0
# # while True:
# #     n = input("enter equation to evaluate : ")
# #         # print(n)
# #     c = n.index('/')
# #     print(c)
# #     # for i in range(len(n)):
# #         # if re.search('/',n) :
# #
# #     # digits = re.split(r'\D', n)
# #     # signs = re.split(r'\d', n)
# #     # print(digits, signs)
