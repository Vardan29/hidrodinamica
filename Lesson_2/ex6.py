def f(x): return x ** 3 + 2 * x + 2


def df(x): return 3 * x * x + 2


def pnf(x): return x - f(x) / df(x)


prev_x = 0.6
next_x = pnf(prev_x)
eps = 10e-8

while abs(next_x - prev_x) > eps:
    prev_x = next_x
    next_x = pnf(prev_x)

print(next_x)
