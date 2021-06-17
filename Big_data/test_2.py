from scipy import sparse

import data_get
import numpy as np

if __name__ == '__main__':
    matrix = np.array(
        [[1, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 0, 0, 1, 1, 0], [0, 0, 0, 1, 0, 1]])
    my_matrix = sparse.csr_matrix(matrix)
    my_matrix = my_matrix.astype(float)
    u, s, vt = data_get.svd(my_matrix, k=3)
    u = u.real
    vt = vt.real
    print('u：', u)
    print('v：',vt)
    print('ok')
