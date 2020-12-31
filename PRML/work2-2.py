import numpy as np

if __name__ == '__main__':
    w_1 = np.array([[0, 0, 0], [1, 0, 0], [1, 0, 1], [1, 1, 0]])
    w_2 = np.array([[0, 0, 1], [0, 1, 1], [0, 1, 0], [1, 1, 1]])
    c = 1
    w_2 *= -1
    w_all = np.vstack((w_2, w_1))
    w = np.array([0, 0, 0])
    flag = [-1] * (w_all.shape[0])
    i = 0
    while -1 in flag:
        i %= len(flag)
        x = w_all.data.obj[i]
        res = np.dot(x, w)
        if res > 0:
            flag[i] = 0
        else:
            w += x
            flag[i] = -1
        i += 1
        print('{0}\t{1}\t{2}\t{3}'.format(i, res > 0, w, flag))
    print(w)
