import numpy as np

def axis_projection(self):
        all_results = []

        for v in self.vectors_std:  # 遍历每个标准向量
            result = []
            for i in range(self.axis.shape[1]):
                u = self.axis[:, i]
                value = np.dot(u, v) / np.linalg.norm(u)
                result.append(value)
            all_results.append(result)
        return np.array(all_results)

A = np.array([[1,1],[0,1]])
# for i in range(A.shape[1]):
#     print(A[:, i])

print(np.linalg.inv(A))
