import numpy as np

class logic_regression:
    def __init__(self, lr = 0.1, epochs = 5000):
        '''
        lr 学习率
        epochs 迭代次数
        '''
        self.lr = lr
        self.epochs = epochs

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-np.clip(z, -250, 250)))
    
    def fit(self, X, y):
        # 在 X 第一列加上全为 1 的常数列
        X = np.insert(X, 0, 1, axis=1)
        m, n = X.shape # m个样本，n个特征
        y = y.reshape(-1, 1) # 转为列矩阵
        self.w = np.zeros((n, 1))

        for _ in range(self.epochs):
            # 预测值 h
            h = self.sigmoid(np.dot(X, self.w))
            gradient = (1/m) * (X.T @ (h - y))
            self.w -= self.lr * gradient
    
    def predict(self, X, rate):
        X = np.insert(X, 0, 1, axis=1)
        # 预测概率大于 rate 即视为好酒
        return (self.sigmoid(X @ self.w) >= rate).astype(int)
    
    def accuracy(self, X, rate, y_test):
        accuracy = np.mean(self.predict(X, rate).flatten() == y_test)
        print(f"准确率: {accuracy * 100:.2f}%")