import math


def f(x, y):
    b = 0.3
    A = 5
    r = (x - 0.5) ** 2 + (y - 0.5) ** 2
    return A * math.exp(-b * r)


def getResult(NX, NY, NZ):
    u = [[[0 for i in range(NY)] for j in range(NX)] for k in range(NZ)]

    lx = ly = 1

    hx = lx / (NX - 1)
    hy = ly / (NY - 1)

    x = [0] * NX
    y = [0] * NY

    tau = 0.25 * (hx ** 2 + hy ** 2)


    for i in range(1, NX):
        x[i] = (i - 1) * hx
    for j in range(1, NX):
        y[j] = (j - 1) * hy

    for k in range(1, NZ):
        for i in range(NY):
            for j in range(NX):
                if i == 0 or j == 0 or i == NY - 1 or j == NX - 1:
                    u[k][i][j] = 0

    gammaX = tau / hx ** 2
    gammaY = tau / hy ** 2

    for k in range(NZ-1):
        for i in range(1,NY-1):
            for j in range(1,NY-1):
                u[k+1][i][j] = (1 - 2 * gammaX - 2 * gammaY) * u[k][i][j] + gammaX * (u[k][i+1][j]+u[k][i-1][j])+ gammaY*(u[k][i][j+1]+u[k][i][j-1])+tau * f(x[i],y[j])

    for k in range(NZ):
        for i in range(NY):
            print(u[k][i])
        print()


getResult(10,10,10)
