k = 1000
y = [0] * k
y[0] = 4
t = [0] * k
t[0] = 2
h = 0.2
i = 0

while i < k - 1:
    t[i + 1] = t[i] + h
    i += 1
i = 0


def f(t, y): return ((2 * t - 5) * y) / (t ** 2) + 5


while i < k - 1:
    y[i + 1] = y[i] + h * f(t[i], y[i])
    i += 1

z = [0] * k

for j in range(len(z) - 1):
    z[j] = y[j] + h / 2 * (f(t[j], y[j]) + f(t[j + 1], y[j + 1]))
    print(y[j] - z[j], end=" ")
