__author__ = 'pavan'


"""ax^2+bx+c = 0 is a quadtractic equation
"""
import cmath
a = float(raw_input("enter the coefficient of x^2 : "))
b = float(raw_input("enter the coefficient of x : "))
c = float(raw_input("enter the constant : "))

e = b**2 - 4 *a*c

f = (-b + cmath.sqrt(e))/(2*a)
g =  (-b - cmath.sqrt(e))/(2*a)
print "the roots of the equation is : ",f,g




