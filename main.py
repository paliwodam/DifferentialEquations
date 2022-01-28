from matplotlib import pyplot as plt
from diff_eq import solve
from time import time
import numpy as np


def draw_plot(n):
    a = 0
    b = 2
    x_values = np.linspace(a, b)
    y_values = list(map(solve(n), x_values))

    plt.plot(x_values, y_values)
    plt.show()


n = 1000
draw_plot(n)

