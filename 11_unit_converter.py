# -*- coding: utf-8 -*-


def length_converter():
    print("length converter")
    a = float(input("enter length value: "))
    x = input("from(km/m/cm/mi/f/i/y/nm): ")
    y = input("to(km/m/cm/mi/f/i/y/nm): ")

    l = {'km': 1, 'm': 1000, 'cm': 100000, 'mi': 0.62137, 'f': 3280.84, 'i': 39370.1, 'y': 1093.61, 'nm': 0.5399}
    print(a * l[y] / l[x])


def volume_converter():
    print("volume converter")
    a = float(input("enter volume value: "))
    x = input("from(l/ml/g/c/ts/b): ")
    y = input("to(l/ml/g/c/ts/b): ")

    c = {"l": 1, "ml": 1000, "g": 0.2642, "c": 4, 'ts': 67.628, "b": 0.00629}
    print(a * c[y] / c[x])


def mass_converter():
    print("mass converter")
    a = float(input("enter mass value: "))
    x = input("from(k/g/t/p/o): ")
    y = input("to(k/g/t/p/o): ")

    m = {'k': 1, 'g': 1000, 't': 0.001, 'p': 2.2046, 'o': 35.274}
    print(a * m[y] / m[x])


def currency_converter():
    print("currency converter")
    a = float(input("enter currency value: "))
    x = input("from(ad/e/ir/gbp/cy/rr/uaed): ")
    y = input("to(ad/e/ir/gbp/cy/rr/uaed): ")

    c = {"ad": 1, "e": 0.90, "ir": 69.03, "gbp": 0.8, 'cy': 6.88, "rr": 63.12, "uaed": 3.67}
    print(a * c[y] / c[x])


def temp_converter():
    print("temperature converter")
    a = float(input("enter temperature value: "))
    x = input("from(c/f/k): ")
    y = input("to(c/f/k): ")
    if x == 'c' and y == 'f':
        print("{}\xb0C = {}\xb0F".format(a, ((a * 9 / 5) + 32)))
    elif x == 'f' and y == 'c':
        print("{}\xb0F = {}\xb0C".format(a, (a - 32) * 5 / 9))
    elif x == 'c' and y == 'k':
        print("{}\xb0C = {}K".format(a, a + 273.15))
    elif x == 'k' and y == 'c':
        print("{}K = {}\xb0C".format(a, a - 273.15))
    elif x == 'f' and y == 'k':
        print("{}\xb0F = {}K".format(a, (a - 32) * 5 / 9 + 273.15))
    elif x == 'k' and y == 'f':
        print("{}K = {}\xb0F".format(a, (a - 273.15) * 9 / 5 + 32))


print("Select operation.")
print("1.length converter")
print("2.volume converter")
print("3.mass converter")
print("4.currency converter")
print("5.temperature converter")

while True:
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("length_converter selected")
        length_converter()
    if choice == 2:
        print("volume_converter selected")
        volume_converter()
    if choice == 3:
        print("mass_converter selected")
        mass_converter()
    if choice == 4:
        print("currency_converter selected")
        currency_converter()
    if choice == 5:
        print("temp_converter selected")
        temp_converter()
    else:
        print("not selected")
        break


# length_converter
# volume_converter
# mass_converter
# currency_converter
# temp_converter
