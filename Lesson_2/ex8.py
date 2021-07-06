# x^4 + 3x^3 + 3x^2 - x - 6 = 0


import math


def f(x): return x ** 4 + 3 * x ** 3 + 3 * x ** 2 - x - 6


def df(x): return 4 * x * 3 + 9 * x * 2 + 6 * x - 1


def pnf(x): return x - f(x) / df(x)


prev_x = 0.6
next_x = pnf(prev_x)
eps = 10e-8

while abs(next_x - prev_x) > eps:
    prev_x = next_x
    next_x = pnf(prev_x)

print(next_x)

prev_x = -0.6
next_x = pnf(prev_x)

while abs(next_x - prev_x) > eps:
    prev_x = next_x
    next_x = pnf(prev_x)

print(next_x)
