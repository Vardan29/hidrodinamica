import numpy as np

k = 1000
y = np.zeros(k)
y[0] = 4
t = np.zeros(k)
t[0] = 2
h = 0.002
i = 0

while i < k - 1:
    t[i + 1] = t[i] + h
    i += 1
i = 0

while i < k - 1:
    f = ((2 * t[i] - 5) * y[i]) / (t[i] ** 2) + 5
    y[i + 1] = y[i] + h * f
    i += 1

print(y)
