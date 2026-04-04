import numpy as np

class svm:
    def __init__(self, lr=0.01, steps=1000, regular_parameter = 0.01):
        '''
        lr 学习率
        steps 迭代次数
        regular_parameter 正则化参数
        w, b超平面系数
        '''
        self.lr = lr
        self.steps = steps
        self.regular_parameter = regular_parameter
        self.w = None
        self.b = None
    
    def fit(self, X, y):
        '''
        X, y 传入训练集
        '''
        n_samples, n_features = X.shape
        self.w = np.zeros(n_features)
        self.b = 0

        # 将 y 分为正类与负类
        y_ = np.where(y <= 0, -1, 1)

        # 梯度下降
        for _ in range(self.steps):
            for idx, x_i in enumerate(X):
                # 判断是否要考虑loss函数
                condition = y_[idx] * (np.dot(x_i, self.w) - self.b) >= 1

                if condition:
                    self.w -= self.lr * (self.w * self.regular_parameter)
                else:
                    self.w -= self.lr * (self.w * self.regular_parameter - np.dot(x_i, y_[idx]))
                    self.b -= self.lr * y_[idx]

    def predict(self, X):
        result = np.dot(X, self.w) - self.b
        return np.sign(result)
    
    def accuracy(self, X, y_true):
        '''
        X, y传入测试集'''
        y_pred = self.predict(X)
        rate = np.sum(y_true == y_pred) / len(y_true)
        print(f"SVM 测试集准确率: {rate * 100:.2f}%")