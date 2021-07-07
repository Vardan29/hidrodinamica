import math

a = 1
b = 3
n = 1000

h = (b - a) / n


def f(x): return (3 * x ** 2 - math.sqrt(x))


sq = (f(a) + f(b)) / 2
sum = 0

i = 1
while i < n:
    a += h
    sum += f(a)
    i += 1

result = h * (sq + sum)
print(result)
