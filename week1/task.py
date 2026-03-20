import numpy as np
import json

class axis:
    '''处理四则坐标系运算的类'''
    def __init__(self, basis, vectors):
        self.axis = np.array(basis)
        self.inv_axis = np.linalg.inv(self.axis) # 矩阵求逆
        self.vectors = np.array(vectors)

        # 将坐标转换成原始坐标轴的表示形式
        self.vectors_std = np.dot(self.vectors, self.axis.T) 

    def change_axis(self, A):
        '''坐标系转移'''
        # 行列式判断坐标系是否合法
        if np.linalg.det(A) == 0: 
            raise ValueError("目标坐标系不合法!") 
        
        self.axis = np.array(A)
        self.inv_axis = np.linalg.inv(A)

        # 矩阵乘法转换成新坐标轴的表示
        self.vectors = np.dot(self.vectors_std, self.inv_axis.T)
        print(self.vectors)
    
    def area (self):
        '''坐标系面积/体积'''
        return abs(np.linalg.det(self.axis)) # 直接行列式计算

    def axis_projection(self):
        '''坐标系投影'''
        all_results = [] # 存储所有向量的结果

        for v in self.vectors_std:  # 遍历每个标准向量
            result = [] # 存储单个向量的结果
            for i in range(self.axis.shape[1]):
                u = self.axis[:, i]
                value = np.dot(u, v) / np.linalg.norm(u)
                result.append(value) # 将 value 添加到result里面
            all_results.append(result) # 将 result 添加到all_result里面
        return np.array(all_results)

    def axis_angle(self):
        '''坐标系夹角'''
        all_results = []

        for v in self.vectors_std:  # 遍历每个标准向量
            result = []
            for i in range(self.axis.shape[1]):
                u = self.axis[:, i]
                cos = np.dot(u, v) / (np.linalg.norm(u)*np.linalg.norm(v)) # 计算出余弦值
                value = np.arccos(cos) # 反三角函数计算角度
                result.append(value)
            all_results.append(result)
        return np.array(all_results)

def read_json(data, num):
    '''
    读取数据并根据任务类型执行操作
    data 表示读取的文件名
    num 表示进行第几个group的操作(从1开始)
    '''
    group = data[num-1]
    a = axis(group["ori_axis"], group["vectors"]) # 构建对象

    print("group_name:")
    print(group["group_name"])
    
    # 遍历 tasks 完成所有任务
    for task in group["tasks"]:
        task_type = task["type"]

        if task_type == "axis_angle":
            print("axis_angle:")
            print(a.axis_angle())
        
        elif task_type == "change_axis":
            new_axis = task["obj_axis"]
            print("change_axis:")
            a.change_axis(new_axis)
        
        elif task_type == "axis_projection":
            print("axis_projection:")
            print(a.axis_projection())
        
        elif task_type == "area":
            print("area:")
            print(a.area())
        
        else:
            print("Unknown!") 
            
with open('data(1).json', 'r') as f:
    data = json.load(f)

read_json(data, 15)

