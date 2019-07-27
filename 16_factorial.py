n = int(input("enter number: "))

# using loop
ans = 1
for i in range(1, n + 1):
    ans *= i
print(ans)


# using recursion


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(n))
