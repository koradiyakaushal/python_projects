x = int(input("How many number of digits of fibonacci numbers you want to display? : "))
n1 = 1
n2 = 1


def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(1, x+1):
    print(fib(i), sep='')
