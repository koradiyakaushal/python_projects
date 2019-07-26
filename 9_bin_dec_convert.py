i = input('D TO B(1) OR B TO D(2): ')
if i == '1':
    n = int(input("enter decimal number: "))
    d = []
    x = str(n)
    print(x)
    while n > 0:
        if n % 2 == 0:
            d.append('0')
            n = n // 2
        else:
            d.append('1')
            n = n // 2
    # print(n)
    # d = list(int(i) for i in str(x))
    print("binary of {} is ".format(x, d[::-1]), end='')
    for i in d[::-1]:
        print(i, end="")


elif i == '2':
    n = input("enter binary number: ")
    d = list(int(i) for i in n)
    ans = 0
    d = d[::-1]

    for i in range(len(d)):
        if d[i] == 1:
            ans += 2**i

    print("decimal of {} is {}".format(n, ans))
