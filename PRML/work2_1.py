import numpy as np
import matplotlib.pyplot as plt


def _plot():
    pass


if __name__ == '__main__':
    x = np.arange(-10, 10.0, 0.25)

    # y1 = -0.33 * x + 60
    y2 = 1 - x
    y3 = x - 1
    #
    # y4 = np.minimum(y1, y2)
    # y5 = np.minimum(y2, y3)
    # y7 = np.minimum(y4, y5)

    # plt.fill_between(x, 0, y7, where=y7 <= y3, facecolor='grey', alpha=0.5)
    plt.vlines(0, -10, 10, label=r'$d_1(x)$')
    # plt.plot(0, y1, label=r'$y = -0.33*x+60$')
    plt.plot(x, y3, label=r'$d_3(x)$')
    plt.plot(x, y2, label=r'$d_2(x)$')

    plt.xlabel(r'$x_1$')
    plt.ylabel(r'$x_2$')
    plt.legend()
    plt.show()
