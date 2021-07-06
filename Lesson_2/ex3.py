# x = (x+1)^3

import numpy as np

x = 0
x_L = -3
x_R = -2
eps = 10e-8


def f(x): return x-(x+1)**3


while np.abs(x_L - x_R) > eps:
    x = (x_L + x_R) / 2
    if f(x_L) * f(x) < 0:
        x_R = x
    if f(x) * f(x_R) < 0:
        x_L = x

print(x)
