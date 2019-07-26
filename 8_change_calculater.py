n = int(input("enter value: "))

if n >= 10:
    print('10 rupee: ', n//10)
    n = n % 10

if n >= 5:
    print('5 rupee: ', n//5)
    n = n % 5

if n >= 2:
    print('2 rupee : ', n//2)
    n = n % 2

if n >= 1:
    print('1 rupee: ', n//1)
    n = n % 1
