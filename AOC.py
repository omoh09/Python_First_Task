#Create Basic Calculator for Area of a Circle


import math
from math import pi

while True:
    try:
        print('''
        Write a Python program which accepts the radius
        of a circle from the user and computes the area.
''')
        radius = float(input ("Input the radius of the circle : "))
        cal = float(pi * radius**2)
        print ("The area of the circle with radius ", radius, "is: ", round(cal,2), "\n")
    except ValueError:
        print("Must be a digit")
        quit();
