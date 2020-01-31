import math


def volume(radius):
    return (4 / 3) * math.pi * radius ** 3


r = int(input("Enter the radius of sphere : "))
print("Volume of sphere with radius ", r, " -> %.3f" % volume(r))
