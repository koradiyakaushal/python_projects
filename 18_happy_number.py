n = int(input("enter number to check happy number? "))


def is_happy_number(num):
    rem = sum = 0

    while num > 0:
        rem = num % 10
        sum = sum + (rem * rem)
        num = num // 10
    return sum


num = n
result = num

while result != 1 and result != 4:
    result = is_happy_number(result)

if result == 1:
    print(str(num) + " is a happy number")
elif result == 4:
    print(str(num) + " is not a happy number")
