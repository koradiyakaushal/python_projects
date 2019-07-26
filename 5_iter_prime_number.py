import sys
# print(sys.maxsize)

def chk_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True
# def want_more(y):
#     if y == 'y':
#         return True
#     else:
#         return False
j = 'y'
for i in range(2, sys.maxsize):
    # print("i",i)

    if j == "y":
        if chk_prime(i):
            print(i)
            j = input("y: ")
        else:
            # f = 0
            # print(f)
            continue
    else:
        break






        # l.append(i)
        # break

# a = iter(l)

# while True:
#     j = input("y: ")
#     if j == "y":
#         print(next(a))
#     else:
#         break
