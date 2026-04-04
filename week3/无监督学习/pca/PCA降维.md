[什么是PCA降维](https://www.bilibili.com/video/BV1QS4y1e7y6/?spm_id_from=333.337.search-card.all.click)
## 核心思想
在尽量减少信息损失的前提下，把高维数据压扁到低维空间
- 本质：找一组新的坐标轴，让数据在这些方向上的**方差最大**

---
## 用途
- **数据可视化**
- 提升模型性能：去除冗余特征、减小噪声
## 步骤
### 去中心化
数据的相对位置不影响PCA，去中心化后数据均值为0，方便计算
步骤：
- 计算每一维的均值  
- 每个样本减去均值  
- 得到新的数据矩阵
即将计算出来的每一维均值后得到的中心点作为坐标原点[![peYpWL9.png](https://s41.ax1x.com/2026/04/02/peYpWL9.png)](https://imgchr.com/i/peYpWL9)
### 协方差矩阵
设把数据投影到方向$w$上：

$$z_i = w^T x_i​$$
投影后的方差：
$$\mathrm{Var}(z) = \frac{1}{m} \sum_{i=1}^{m} (w^T x_i)^2$$
标量的转置等于其本身，$(w^T x_i)$ 是一个标量，将后一个$(w^T x_i)$ 转置：
$$(w^T x_i)(w^T x_i) = w^T x_i \cdot x_i^T w = w^T (x_i x_i^T) w$$
转换后的方差：

$$\mathrm{Var}(z) = \frac{1}{m} \sum w^T (x_i x_i^T) w$$
最后的协方差矩阵：
$$\mathrm{Var}(z) = w^T S w$$
$$S = \frac{1}{m} \sum_{i=1}^m x_i x_i^T$$
> S 为一个矩阵
### 求最大方差
#### 加入约束条件
$w^Tw = 1$（若可以把$w$放大，方差就能无限大）
#### 构造函数
转化为无约束问题，直接求导计算
$L(w, \lambda) = w^T S w - \lambda (w^T w - 1)$
#### 求导
对 $w$ 求导并令其为 $0$（极值点）： $$ \frac{\partial L}{\partial w} = 2Sw - 2\lambda w = 0 $$ 整理得到： $$ Sw = \lambda w $$
求解：
$$ (S - \lambda I)w = 0 $$
$(S - \lambda I)w$ 行列式为0解出 $\lambda$，再带入解出$w$
### 选取多个主成分
假设$S$是 n 维方阵，则能求出来n对$\lambda$与$w$
- 排序 
$$ \lambda_1 \geq \lambda_2 \geq \dots $$
- 选前 k 个 
$$ W = [w_1, w_2, \dots, w_k] $$
> k 为要降到的维度
### 得出最后公式
$Z = XW$
