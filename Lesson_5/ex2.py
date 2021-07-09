import math
import time


def getTime(func):
    def getFuncTime(N):
        st = time.time()
        res = func(N)
        et = time.time()
        # print(N, et - st, sep=' ; ')
        return res

    return getFuncTime


# @getTime
def getCalc(N):
    a, b = 0, 1

    J = 10 + 2 * N ** 2
    x = [0] * N
    t = [0] * J

    f = [[0 for i in range(J)] for j in range(N)]

    h = (b - a) / (1.0 * N)
    tau = (b - a)/J

    for i in range(N):
        x[i] = i * h
    for i in range(J):
        t[i] = i * tau

    for i in range(N):
        f[i][0] = math.sin((3 * math.pi * x[i]) / 2)

    for i in range(J - 1):
        f[0][i] = 0
        f[-1][i + 1] = 4 / 3 * f[-2][i + 1] - 1 / 3 * f[-3][i + 1] + (2 * h * t[i] + 1) / 3

    for i in range(1, N - 1):
        for j in range(J - 1):
            f[i][j + 1] = f[i][j] + (tau / h ** 2) * (f[i + 1][j] - 2 * f[i][j] + f[i - 1][j]) + tau * x[i]


    for i in range(N):
        for j in range(J):
            print(x[i],t[j],f[i][j], sep=";")
    return f


# for i in range(100,1000,100):

getCalc(20)

