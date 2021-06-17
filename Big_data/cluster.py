import numpy as np
import pandas as pd
from scipy.sparse import coo_matrix, save_npz, load_npz
from matplotlib import pyplot as plt
from queue import PriorityQueue
import pickle


class Cluster:
    def __init__(self):
        self.topo_dict = pickle.load(open('topo_dict.pkl', 'rb'))
        self.topo = load_npz('topo.npz')
        self.topo = self.topo.tocsr()
        self.attr = np.load('attr.npy')

        print('Prepared.')

        # threshold (including)
        self.threshold_sim = 4
        self.threshold_dis = 500
        self.threshold_clu = 1

        print('Shape:', self.topo.shape, self.attr.shape)
        print("Mean length:", np.mean(self.attr[:, 1]))

        # -1:Unclassified 0:Noise >0:ClusterId
        self.label = np.ones(self.attr.shape[0]) * (-1)
        self.label_count = 1

    def run(self):
        for i in range(len(self.label)):
            if self.label[i] == -1:
                if self.expand_cluster(i):
                    self.label_count += 1
                    print(self.label_count, np.sum(self.label == -1))

        print('Unclassified:', np.sum(self.label == -1))
        print('Noise:', np.sum(self.label == 0))
        np.save('topo_cluster_{:d}_{:d}_{:d}.npy'.format(self.threshold_dis, self.threshold_sim, self.threshold_clu),
                self.label)

        print('Dis =', self.threshold_dis)
        print('Sim =', self.threshold_sim)
        print('Clu =', self.threshold_clu)
        print('Finished.')

    def attr_sim(self, num, j):
        ans = 0
        ans += np.sum(self.attr[num, 2:6] == self.attr[j, 2:6])
        ans += np.sum(self.attr[num, 7:8] == self.attr[j, 7:8])
        if np.abs(self.attr[num, 6] - self.attr[j, 6]) < 1e-7:
            ans += 1
        if np.abs(self.attr[num, 8] - self.attr[j, 8]) < 0.1:
            ans += 1
        return ans

    # topo directed (0.5*length1 + 0.5*length2)
    def topo_dis(self, i, j):
        if self.topo[self, i, j] > 0:
            return (self.attr[i, 1] + self.attr[j, 1]) / 2
        else:
            return np.inf

    # return a list of id <= dis
    def dijkstra(self, i):  # , dis, sim, topo_dict, self.attr
        que = PriorityQueue()
        ans = set()
        ans.add(i)
        que.put((0, i))
        while not que.empty():
            t_dis, t = que.get()
            if t not in self.topo_dict.keys():
                continue
            t_list = self.topo_dict[t]
            for t_next in t_list:
                if t_next in ans:
                    continue
                t_next_dis = self.topo_dis(t, t_next)
                assert t_next_dis < np.inf
                if (t_dis + t_next_dis <= self.threshold_dis) and (self.attr_sim(t, t_next) >= self.threshold_sim):
                    ans.add(t_next)
                    # print(t_dis+t_next_dis)
                    que.put((t_dis + t_next_dis, t_next))
        ans = list(ans)
        ans.sort()
        return ans

    # return True/False for expanding a cluster
    def expand_cluster(self, i):
        seed_list = self.dijkstra(i)
        if len(seed_list) <= self.threshold_clu:
            self.label[i] = 0
            return False
        else:
            for seed in seed_list:
                self.label[seed] = self.label_count
            seed_list.remove(i)
            while len(seed_list) > 0:
                cur = seed_list[0]
                res_list = self.dijkstra(cur)
                if len(res_list) > self.threshold_clu:
                    for res in res_list:
                        if self.label[res] <= 0:
                            if self.label[res] == -1:
                                seed_list.append(res)
                            self.label[res] = self.label_count
                seed_list.remove(cur)
            return True


if __name__ == '__main__':
    cluster = Cluster()
    cluster.run()
    '''
    Total: 
    686105
    
    500_6_1
    Noise: 9360
    Class: 42256
    
    500_5_1
    Noise: 7792
    Class: 23034
    
    500_4_1
    Noise: 7146
    Class: 15082
    
    '''
