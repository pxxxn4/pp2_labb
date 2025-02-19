from math import *

def deg_to_rad():
    d = float(input("Input degree: "))
    print(f'Output radians {radians(d):.6f}')

def trap_area():
    h = float(input("Height: "))
    a = float(input("Base, first value: "))
    b = float(input("Base, second value: "))

    res = (1/2) * (a + b) * h
    print(f'Area = {res:.2f}')

def poly_area():
    n = int(input('Input number of sides: '))
    l = float(input('Input the length of a side: '))

    apo = l / (2 * tan(pi/n))
    res = (n * l * apo) / 2

    print(f'The area of the polygon is {res:.2f}')

def para_area():
    b = float(input("Length of base: "))
    h = float(input("Height of parallelogram: "))
    res = b * h
    print(f"Area = {res:.2f}")
