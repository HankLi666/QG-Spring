import numpy as np
import pandas as pd
from svm import svm
from sklearn.datasets import load_iris

# 加载iris数据集
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
df['species'] = df['target'].map({i: name for i, name in enumerate(iris.target_names)})

# svm是二分类，所以只取前2种花
df = df[df['species'].isin(['setosa', 'versicolor'])]

# 提取特征和 标签
X = df.iloc[:, 0:4].values  # 前 4 列是特征
y = df.iloc[:, 4].values    # 最后一列是标签

# 特征编码将字符串转为 [-1, 1]
y = np.where(y == 'setosa', 1, -1)

# 数据归一化
X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

# 设置随机种子保证结果可复现
np.random.seed(42)

# 生成打乱的索引
indices = np.random.permutation(X.shape[0])

# 计算切分点
split_idx = int(X.shape[0] * 0.8)
train_idx, test_idx = indices[:split_idx], indices[split_idx:]
X_train, X_test = X[train_idx], X[test_idx]
y_train, y_test = y[train_idx], y[test_idx]

model = svm(lr=0.001, steps=1000, regular_parameter = 0.01)

model.fit(X_train, y_train)

model.accuracy(X_test, y_test)