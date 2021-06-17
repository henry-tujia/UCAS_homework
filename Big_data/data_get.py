import spartan as st
import pandas as pd
import numpy as np
from scipy import sparse
from scipy.sparse import linalg


def save(matrix, name):
    df_save = pd.DataFrame(matrix)
    columns = [name + '-' + str(i) for i in range(1, matrix.shape[1] + 1)]
    df_save.columns = columns

    df_save.to_csv(name + '.csv', sep='\t', encoding='utf-8', index=False)
    print(name + 'is done!')


def svd(martix, k):
    martix_n = martix.dot(martix.T)
    martix_n_ = martix.T.dot(martix)

    eval_sigma1, evec_u = linalg.eigs(martix_n, k)
    eval_sigma1 = np.sqrt(eval_sigma1)
    _, evec_v_t = linalg.eigs(martix_n_, k)

    return evec_u, eval_sigma1, evec_v_t


def creat_martix(data_df):
    ids = data_df['column1'].tolist()
    cities = data_df['column2'].tolist()
    labels = [1] * len(ids)
    matrix = sparse.coo_matrix((labels, (ids, cities)), dtype=float)

    return matrix


if __name__ == '__main__':
    tensor_data = st.loadTensor(path="./yelp.edgelist.gz")
    data = tensor_data.Data[:]
    data_ = data[0].map(lambda x: [int(s) for s in x.split(' ') if s != ' ']).values.tolist()

    data_df = pd.DataFrame(data=data_)
    data_df.columns = ['column1', 'column2', 'label']
    c = creat_martix(data_df)

    u, s, vt = svd(c, k=10)
    save(u.real, 'U')
    save(vt.real, 'V')

    print('ok')
