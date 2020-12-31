import numpy as np

if __name__ == '__main__':
    w_1 = np.array([[1, 0], [2, 0], [1, 1]])
    w_2 = np.array([[-1, 0], [0, 1], [-1, 1]])
    w_3 = np.array([[-1, -1], [0, -1], [0, -2]])

    mean_1 = np.mean(w_1, axis=0)
    mean_2 = np.mean(w_2, axis=0)
    mean_3 = np.mean(w_3, axis=0)

    mean = np.mean(np.vstack((mean_1, mean_2, mean_3)), axis=0)

    s_w = np.matmul(w_1 - mean_1, (w_1 - mean_1).T) / w_1.shape[0] + np.matmul(w_2 - mean_2, (w_2 - mean_2).T) / \
          w_2.shape[0] + np.matmul(w_3 - mean_3, (w_3 - mean_3).T) / w_3.shape[0]

    s_b = np.matmul(mean_1.reshape(-1, 1) - mean.reshape(-1, 1),
                    (mean_1.reshape(-1, 1) - mean.reshape(-1, 1)).T) + np.matmul(
        mean_2.reshape(-1, 1) - mean.reshape(-1, 1), (mean_2.reshape(-1, 1) - mean.reshape(-1, 1)).T) \
          + np.matmul(mean_3.reshape(-1, 1) - mean.reshape(-1, 1), (mean_3.reshape(-1, 1) - mean.reshape(-1, 1)).T)
    s_b *= 1 / 3
    print(s_w)
    print(s_b)
    print('ok')
