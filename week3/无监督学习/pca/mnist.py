from sklearn import datasets
import matplotlib.pyplot as plt
from PCA import PCA

# 加载MNIST数据集
mnist = datasets.fetch_openml("mnist_784", version=1)

# 获取数据和标签
X = mnist.data.values  # 28x28的像素数据（784维）
y = mnist.target.astype(int)  # 标签（0-9数字）

# 使用PCA将数据降到二维
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
print(X_pca.shape)

# 可视化
plt.figure(figsize=(10, 8))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis', edgecolor='k', s=20)
plt.colorbar(label='Digit')
plt.title("PCA of MNIST Dataset")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.show()