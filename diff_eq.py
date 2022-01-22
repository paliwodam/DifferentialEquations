from numpy.linalg import inv
from functools import partial
from math import sin

import scipy.integrate as integrate
import numpy as np

a = 0
b = 2


def B(u, v):
    return v(b) * u(b) + integrate.quad(lambda x: -v(x) * u(x), a, b)[0]


def L(v):
    return integrate.quad(lambda x: sin(x) * v(x), a, b)[0]


def f_linear(a, b):
    return lambda x: a * x + b


def get_e(n):
    e = []
    for i in range(1, n + 2):
        a = n + 1
        b = 1 - i
        e.append(partial(f_linear(a, b)))

    return e


def get_arrays(B, L, e):
    a_B = np.array([[B(u, v) for u in e] for v in e])
    a_L = np.array([L(v) for v in e])

    return a_B, a_L


def get_a_u(a_B, a_L):
    return inv(a_B).dot(a_L)


def union_f_g(f, g):
    return lambda x: f(x) + g(x)


def solve(n):
    e = get_e(n)
    a_B, a_L = get_arrays(B, L, e[0:n])
    a_u = get_a_u(a_B, a_L)

    u = lambda x: e[n](x)
    for i in range(n):
        u = union_f_g(u, lambda x: e[i](x) * a_u[i])

    return u

