import numpy as np

class PCA:
    def __init__(self, n_components):
        '''
        n_components 降维后的目标维度
        '''
        self.n_components = n_components
    
    def fit(self, X):
        # 去中心化
        self.mean = np.mean(X, axis=0)
        X_centered = X - self.mean

        # 协方差矩阵
        matrix = np.cov(X_centered, rowvar=False)

        # 特征值分解
        values, w = np.linalg.eigh(matrix)

        # 特征值排序
        sorted_idx = np.argsort(values)[::-1]  # 降序排列
        values = values[sorted_idx]
        w = w[:, sorted_idx]

        # 选取前 n 个主成分
        self.W = w[:, :self.n_components]

    def transform(self, X):
        '''
        对应 Z = XW
        '''
        X_centered = X - self.mean
        return np.dot(X_centered, self.W)
    
    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)