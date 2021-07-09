import math
import time


def getTime(func):
    def getFuncTime(N):
        st = time.time()
        res = func(N)
        et = time.time()
        #print(N, et - st, sep=' ; ')
        return res
    return getFuncTime


@getTime
def getCalc(N):
    a, b = 0, 1

    x = [0] * N
    t = [0] * N

    f = [[0 for i in range(N)] for j in range(N)]

    h = (b - a) / (1.0 * N)
    tau = h

    for i in range(N):
        x[i] = i * h
        t[i] = i * tau

    for i in range(N - 1):
        f[i][0] = math.cos(math.pi * x[i])
        f[i][1] = f[i][0] + tau * x[i] ** 2 - 0.5 * (math.pi * tau) ** 2 * math.cos(math.pi * x[i])

    f[0][0] = f[1][0]
    f[-1][0] = f[-2][0]

    f[0][1] = f[1][1]
    f[-1][1] = f[-2][1] + 2 * h * math.sin(tau)

    for j in range(1, N - 1):
        for i in range(1, N - 1):
            f[i][j + 1] = 2 * f[i][j] - f[i][j - 1] + (f[i + 1][j] - 2 * f[i][j] + f[i - 1][j]) - (
                        tau * x[i]) ** 2 * math.sin(t[j])
        f[0][j + 1] = f[1][j + 1]
        f[N - 1][j + 1] = f[N - 2][j + 1] + 2 * h * math.sin(t[j + 1])

    for i in range(N):

        print(x[i],f[i][int(N/2)],sep=";")

    return f

# for i in range(100,1000,100):
getCalc(1000)
