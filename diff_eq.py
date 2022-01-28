from numpy.linalg import inv
from math import sin

import scipy.integrate as integrate
import numpy as np


def B(u, v):
    a1, b1, a2, b2 = u[2], u[3], v[2], v[3]
    if b1 >= a2 >= a1:
        a = a2
        b = b1
    elif b2 >= a1 >= a2:
        a = a1
        b = b2
    else:
        return v[0](2) * u[0](2)
    if a == b:
        return v[0](2) * u[0](2)
    return v[0](2) * u[0](2) - integrate.quad(lambda x: u[1](x) * v[1](x) - v[0](x) * u[0](x), a, b)[0]


def L(v):
    a = v[2]
    b = v[3]
    return -integrate.quad(lambda x: sin(x) * v[0](x), a, b)[0]


def e_i(i, n):
    h = 2 / n
    d1 = 1 - i
    d2 = 1 + i

    a = max(0, h * (i-1))
    b = min(h * (i+1), 2)

    def e(x):
        if a <= x <= h * i:
            return 1 / h * x + d1
        elif h * i < x < b:
            return -1 / h * x + d2
        return 0

    def de(x):
        if a <= x <= h * i:
            return 1 / h
        elif h * i < x < b:
            return -1 / h
        return 0

    return e, de, a, b


def get_e(n):
    e = []
    for i in range(n+1):
        e.append(e_i(i, n))

    return e


def arrays(B, L, e):
    arr_B = np.array([[B(u, v) for u in e] for v in e])
    arr_L = np.array([L(v) for v in e])
    return arr_B, arr_L


def dotArrays(arr_B, arr_L):
    return inv(arr_B).dot(arr_L)


def u(arr_u, e, x):
    res = 0
    for i in range(len(e)):
        res += e[i][0](x) * arr_u[i]
    return res


def solve(n):
    e = get_e(n)
    arr_B, arr_L = arrays(B, L, e)
    arr_u = dotArrays(arr_B, arr_L)

    return lambda x: u(arr_u, e, x)





