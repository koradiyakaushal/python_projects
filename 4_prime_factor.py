n = int(input("Enter number to find prime factor: "))


def chk_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True


for i in range(2, n):
    if n % i == 0:
        if chk_prime(i):
            print(i)
