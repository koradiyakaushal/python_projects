# using Haversine Formula
import math
from math import radians

# default
lon1 = radians(-77.037852)
lat1 = radians(38.898556)
lon2 = radians(-77.043934)
lat2 = radians(38.897147)


def length_converter(a):
    print("length converter")
    # a = float(input("enter length value: "))
    x = 'km'
    y = input("in (km/m/cm/mi/f/i/y/nm): ")

    l = {'km': 1, 'm': 1000, 'cm': 100000, 'mi': 0.62137, 'f': 3280.84, 'i': 39370.1, 'y': 1093.61, 'nm': 0.5399}
    print(a * l[y] / l[x])


# lon1 = float(input("Enter Longitude of city 1: "))
# lat1 = float(input("Enter Latitude of city 1: "))
# lon2 = float(input("Enter Longitude of city 2: "))
# lat2 = float(input("Enter Latitude of city 2: "))
dlon = lon2 - lon1
dlat = lat2 - lat1
R = 6373

a = (math.sin(dlat / 2)) ** 2 + ((math.cos(lat1)) * math.cos(lat2)) * (math.sin(dlon / 2)) ** 2
# print(a)
c = 2 * (math.atan2(math.sqrt(a), math.sqrt(1 - a)))
# print(c)
d = R * c
# print("in kms: ",d)
length_converter(d)
