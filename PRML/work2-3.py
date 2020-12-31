import numpy as np


def mat_max_index(x, w):
    res = [np.dot(x, value) for value in w.data.obj]
    max_item = max(res)
    max_count = res.count(max_item)
    max_index = res.index(max(res)) if max_count == 1 else -1
    return max_index


if __name__ == '__main__':
    O = np.array([[-1, -1], [0, 0], [1, 1]])
    O = np.insert(O, O.shape[1], values=1, axis=1)

    W = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    flag = [-1] * O.shape[0]
    i = 0
    while -1 in flag:
        flag = [-1] * O.shape[0]
        for i, o in enumerate(O):
            if i == mat_max_index(o, W):
                flag[i] = 0
            else:
                for j, w in enumerate(W):
                    if j == i:
                        w += o
                    else:
                        w -= o
    print(W)