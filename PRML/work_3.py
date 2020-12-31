import numpy as np
import sympy

if __name__ == '__main__':
    w_1 = np.array([[0, 1], [0, -1]])
    w_2 = np.array([[1, 0], [-1, 0]])

    w_all = np.vstack((w_1, w_2))
    flag = [-1] * w_all.shape[0]

    x_1, x_2, y_1, y_2 = sympy.symbols('x_1 x_2 y_1 y_2')
    # K = 1 + 4 * x_1 * y_1 + 4 * x_2 * y_2 + 16 * x_1 * x_2 * y_1 * y_2
    K = sympy.exp(-((x_1-y_1)**2+(x_2-y_2)**2))
    i = 0
    flag_first = True
    while -1 in flag:
        i %= len(flag)
        if i > w_1.shape[0]-1:
            isW_1 = -1
        else:
            isW_1 = 1
        w = w_all.data.obj[i]
        if flag_first:
            K_ = K.subs(y_1, w.data.obj[0])
            K_ = K_.subs(y_2, w.data.obj[1])
            K_res = K_
            flag_first = False
        else:
            K_res = K_.subs(x_1, w.data.obj[0]).subs(x_2, w.data.obj[1])
        if not K_res.is_Function:
            if (K_res > 0 and isW_1 == 1) or (K_res < 0 and isW_1 == -1):
                flag[i] = 0
            else:
                K_ += isW_1 * K.subs(y_1, w.data.obj[0]).subs(y_2, w.data.obj[1])
                flag[i] = -1
        i += 1

        print(K_)
