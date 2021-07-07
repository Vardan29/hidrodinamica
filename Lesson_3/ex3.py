import math

eps = 10e-8

N, a, b = 10, 0, 1

x = [0] * N
y = [0] * N
f = [[0 for row in range(N)] for col in range(N)]
h = (b - a) / (1.0 * N)


for i in range(0, N - 1):
    x[i + 1] = x[i] + h
    y[i + 1] = y[i] + h

for i in range(0, N):
    f[0][i] = math.cos(y[i])
    f[-1][i] = math.e * math.cos(y[i])
    f[i][0] = math.exp(x[i])
    f[i][-1] = math.cos(x[i]) * math.cos(x[i])

for i in f:
    print(i)
