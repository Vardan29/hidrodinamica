import math

k = 10

y = [0] * k
x = [0] * k

y[0] = 4
x[0] = y[0]

h = 0.2


def f(x, y): return x + math.cos(y / math.sqrt(10))


for i in range(k - 1):
    x[i + 1] = x[i] + h


for i in range(k - 1):
    k1 = f(x[i], y[i])
    k2 = f(x[i] + h / 2, y[i] + h / 2 * k1)
    k3 = f(x[i] + h / 2, y[i] + h / 2 * k2)
    k4 = f(x[i] + h, y[i] + h * k3)
    y[i + 1] = y[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

print(y)
