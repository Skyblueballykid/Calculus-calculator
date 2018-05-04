import sympy as sym
import math
import numpy as np
from sympy import limit
from sympy import integrate
from sympy import diff

### Solving basic calculus problems using sympy

# 2
f2 = 6/(math.sqrt(6*0+4)+4)
print("Question 2: ", sym.limit(f2,0,0))

# 3
def f3(x3):
    return ((x3 * -3) -18)/((x3**3) + (6 * (x3**2)))
print("Question 3: ", sym.limit(f3(-3),0,-3))

# 9
def f9(x9):
    return(((-3*x9)**3)-(4*x9**2)+2)/(((7*x9)**3)+((4*x9)**2)-(3*x9))
print("Question 9: ", sym.limit(f9(x9=sym.oo),0,sym.oo))

# 10
def f10(x10):
    return(((1-(x10**4))/(x10**2)+(8*x10))**5)
print("Question 10: ", f10(9))

# 13
def f13(x13):
    return(((4*x13)**5)/5)-(3*x13)+(9*math.exp(x13))
print("Question 13: ", sym.diff(f13(9)))
