import re

cc_vendor = ['Visa', 'MasterCard', 'AmericanExpress', 'Discoverer']

# i = input("enter credit card vendor name: ")
n = int(input("enter credit card number: "))
# n = 4556108117123707614
n1 = list(str(n))
cnl = len(n1)
# print(cnl)


def validate(n):
    cc_no = [y for y in str(n)]
    ld = cc_no.pop()
    cc_no = cc_no[::-1]
    # print(cc_no)
    sum = 0

    for x in range(len(cc_no)):
        if x % 2 == 0:
            cc_no[x] = str(int(cc_no[x]) * 2)
        if int(cc_no[x]) > 9:
            cc_no[x] = str(int(cc_no[x]) - 9)
        sum += int(cc_no[x])
    sum += int(ld)
    # print(sum)
    # print(cc_no)

    if sum % 10 == 0:
        print("valid credit card number.")
    else:
        print("INVALID number.")


# print(validate(n))


print("Select vendor.")
print("1.Visa")
print("2.MasterCard")
print("3.AmericanExpress")
print("4.Discoverer")

i = input("enter choice: ")
# n1 = str(n)
if i == '1':
    vl = ''.join(n1[0])
    # print(vl)
    # print(cnl)
    if int(vl) == 4 and (cnl == 16 or cnl == 13 or cnl == 19):
        validate(n)
    else:
        print('invalid')
elif i == '2':
    sl = ''.join(n1[0:2])
    sl2 = ''.join(n1[0:6])
    if 51 <= int(sl) <= 55 or 222100 <= int(sl2) <= 272099 and (cnl == 16):
        # print('s')
        validate(n)
    else:
        print('invalid')

elif i == '3':
    sl = ''.join(n1[0:2])
    if int(sl) == 34 or int(sl) == 37 and (cnl == 15):
        validate(n)
    else:
        print('invalid')

elif i == '4':
    sl = ''.join(n1[0:2])
    sl2 = ''.join(n1[0:3])
    sl3 = ''.join(n1[0:4])
    sl4 = ''.join(n1[0:6])
    if int(sl) == 65 or 644 <= int(sl2) <= 649 or int(sl3) == 6011 or 622126 <= int(sl4) <= 622925 and (16 <= cnl <= 19):
        validate(n)
    else:
        print('invalid')
