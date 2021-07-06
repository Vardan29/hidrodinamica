import numpy as np

k = 10
x = np.zeros(k)
x[0] = 0.6
x[-1] = 1.6
h = 0.1
y = np.zeros(k)
y[0] = 0.8
i = 1

while i < k:
    x[i] = x[i - 1] + h
    i += 1
i = 1
while i < k:
    f = x[i] + np.cos(y[i - 1] / np.sqrt(10))
    y[i] = y[i - 1] + h * f
    i += 1

print(x)
print(y)
