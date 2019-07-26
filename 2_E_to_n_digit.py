import math

n = int(input("How many number of digits of e you want to display? : "))
if n <= 15:
    limit_pi = str(math.e)[0:n + 2]
    print("{}".format(limit_pi))
else:
    print("enter upto 15 digits.")
