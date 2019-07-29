i1 = int(input("Enter first digit: "))
i2 = int(input("Enter second digit: "))
e = 1
print(i1**i2)
# ans = 0
while i2 > 2:
    if i2 % 2 != 0:
        i2 -= 1
        e *= i1
        # print(e)
    else:
        i1 = i1**2
        i2 = i2/2
# print(i1)
print((i1**2)*(e))
