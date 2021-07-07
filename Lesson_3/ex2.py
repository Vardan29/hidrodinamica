import math

a = 1
b = 3
n = 1000

h = (b - a) / n


def f(x): return 3 * x ** 2 - math.sqrt(x)


k1 = (f(a + h) - f(a)) / h
k2 = (f(a + h) - f(a - h)) / (2 * h)

k2_1 = (f(a - h) - 2 * f(a) + f(a + h)) / h ** 2

print(k1, k2, k1 - k2, sep="\n")

print(f"\n{k2_1}")

sq = (f(a) + f(b)) / 2
sum = 0

i = 1
while i < n:
    a += h
    sum += f(a)
    i += 1

result = h * (sq + sum)
print(result)
