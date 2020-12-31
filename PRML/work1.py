import numpy as np


class byers():
    def __init__(self):
        self.w_1 = np.array([[0, 0], [2, 0], [2, 2], [0, 2]])
        self.w_2 = np.array([[4, 4], [6, 4], [6, 6], [4, 6]])
        self.mean_1 = self._get_mean(self.w_1)
        self.mean_2 = self._get_mean(self.w_2)
        self.cov = self._get_cov(self.w_1, self.mean_1)

        self.w, self.b = self._get_line()
        self._plot()

    def _get_mean(self, x):
        return np.mean(x, axis=0)

    def _get_cov(self, x, m):
        return np.matmul((x - m).T, x - m) / x.shape[0]

    def _matmul(self, x, y, z):
        return np.matmul(np.matmul(x, y), z)

    def _get_line(self):
        cov_ = np.linalg.inv(self.cov)
        b = 0.5 * (self._matmul(self.mean_2.T, cov_, self.mean_2) - self._matmul(self.mean_1.T, cov_, self.mean_1))
        w = np.matmul((self.mean_1 - self.mean_2).T, cov_)
        line = ''
        for i, item in enumerate(w.data):
            flag = '+' if item > 0 else ''
            line += flag + str(item) + '*x_' + str(i + 1)
        flag = '+' if b > 0 else ''
        line += flag + str(b)
        print(line)
        return w, b

    def _plot(self):
        import matplotlib.pyplot as plt
        # tem  = self.w_1.data[0]

        x_1 = [x[0] for x in self.w_1.data.obj]
        y_1 = [x[1] for x in self.w_1.data.obj]

        x_2 = [x[0] for x in self.w_2.data.obj]
        y_2 = [x[1] for x in self.w_2.data.obj]

        fig = plt.figure()

        # Make data.
        X = np.arange(0, 8, 0.25)

        a1 = self.w.data[0]
        a2 = self.w.data[1]
        Y = (-a1 * X - self.b) / a2

        # Plot the line.
        plt.plot(X, Y)
        plt.xlabel(r"$x_1$")
        plt.ylabel(r"$x_2$")
        plt.scatter(x_1, y_1, label=r'$w_1$', color=(0., 0.5, 0.))
        plt.scatter(x_2, y_2, label=r'$w_2$', color=(0.5, 0., 0.))
        plt.legend()
        plt.show()


if __name__ == '__main__':
    byr = byers()
