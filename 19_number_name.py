n = int(input("Enter number: "))
w = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
     10: ' Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
     17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty',
     60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety', 100: 'Hundred', 1000: 'Thousand', 100000: 'Lakh '}


def chk_zero(n):
    if n == 0 or n == "":
        return ""
    else:
        return w[n]


def two_digit_str(i):
    if i <= 20:
        return chk_zero(i)
    elif i <= 99:
        ms = i // 10 * 10
        r = i % 10
        s = "{}-{}".format(chk_zero(ms), chk_zero(r))
        return s
        # print('number pronunciation is {} {} '.format(w[m], w[rem]))


def last_third_digit(i):
    l1 = i // 100
    return chk_zero(l1)


if n <= 20:
    print(w[n])

elif n <= 99:
    print('number pronunciation is {}'.format(two_digit_str(n)))

elif n <= 999:

    h2 = n % 100
    # print(h2)
    l2 = two_digit_str(h2)
    # print(h1, h3, h4)
    print('number pronunciation is {} hundred {} '.format(last_third_digit(n), l2))

elif n <= 9999:
    h0 = n // 1000  # 9 thousand
    h1 = n % 1000  # 999
    h2 = last_third_digit(h1)  # 9
    h3 = h1 % 100  # 99
    l2 = two_digit_str(h3)
    h = w[100]
    if h2 == "":
        h = ""

    # print(h0, h2, h4, h5)
    print('number pronunciation is {} Thousand, {} {}, {} '.format(w[h0], last_third_digit(h1), h, l2))

else:
    print("coming soon")
# you can also use below method in answer
# https://stackoverflow.com/questions/8982163/how-do-i-tell-python-to-convert-integers-into-words
