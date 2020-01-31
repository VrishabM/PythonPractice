import math as m


def areaCircle(radius):
    return m.pi * radius * radius


print("Enter Radius of Circle to find area\nEnter 0 to exit")
n = int(input("Input : "))
while n != 0:
    print("Area Of ", n, " = ", areaCircle(n))
    print("Enter Radius of Circle to find area\nEnter 0 to exit")
    n = int(input("Input : "))
