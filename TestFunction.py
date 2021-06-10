from math import *


def f_zero(x):
    return x**3 - 3*np.sin(x)


def f_ones(x):
    return x**3 - 27*x + 5


def f(x):
    return x[0]**2 + 2*x[1]**2 - 0.3*cos(3*pi*x[0]) - 0.4*cos(4*pi*x[1]) + 0.7


def g(x):
    return sin(x[0] + x[1]) + (x[0] - x[1])**2 - 1.5*x[0] + 2.5*x[1] + 1


def h(x):
    return 0.5+((np.sin((x[0]**2+x[1]**2)**2))**2-0.5/1+0.001*((x[0]**2+x[1]**2)**2))
