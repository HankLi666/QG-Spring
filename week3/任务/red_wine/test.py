import numpy as np
import pandas as pd
from linear_regression import linear_regression
from logic_regression import logic_regression

df = pd.read_csv('red_wine/red_wine.csv')

# 提取特征和标签， 标签在最后一行
X = df.iloc[:, :-1].values
y1 = df.iloc[:, -1].values # 线性回归
y2 = (df['quality'] > 6).astype(int).values # 逻辑回归

# 设置随机种子保证结果可复现
np.random.seed(42)
indices = np.arange(X.shape[0])
np.random.shuffle(indices) # 打乱数据

# 计算切分点
split_idx = int(X.shape[0] * 0.8)
train_idx, test_idx = indices[:split_idx], indices[split_idx:]

X_train, X_test = X[train_idx], X[test_idx]
y_train1, y_test1 = y1[train_idx], y1[test_idx]
y_train2, y_test2 = y2[train_idx], y2[test_idx]

# 数据归一化
mean = np.mean(X_train, axis=0)
std = np.std(X_train, axis=0)

# 测试集使用训练集的 mean 和 std，以模拟真实预测场景
X_train = (X_train - mean) / std
X_test = (X_test - mean) / std

# 线性回归
model1 = linear_regression(method='ols', lr=0.01, epochs=5000)
model1.fit(X_train, y_train1)
y_pred1 = model1.predict(X_test)
# 评价
r2 = model1.score(y_test1.reshape(-1, 1), y_pred1)
print('线性回归：')
print(f"测试集 R^2 分数: {r2:.4f}")

# 逻辑回归
model2 = logic_regression(lr = 0.1, epochs=5000)
model2.fit(X_train, y_train2)
print('逻辑回归：')
model2.accuracy(X_test, 0.5, y_test2)

