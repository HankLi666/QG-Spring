## json介绍
json是一种轻量级的数据交换格式，易于人阅读编写与数据传输，同时也易于机器解析和生成
可以灵活的**运用键值对表示树形结构**

---
## json库的导入

```python
import json
```
---
## json语法
### 对象与数组
- **对象**：大括号 {} 保存的对象是一个无序的**名称/值**对集合。一个对象以左括号 { 开始， 右括号 } 结束。每个"键"后跟一个冒号 :，**名称/值**对使用逗号 , 分隔
- **数组**：中括号 [] 保存的数组是值的有序集合。一个数组以左中括号 `[` 开始， 右中括号 ] 结束，值之间使用逗号 , 分隔
>对象与数组均可互相或与自身嵌套
```json
{
  "studio_name": "QG",
  "info": { "building": "教3", "room": 101 },      // 对象内嵌对象
  "tags": ["ai组", "后台组"],                      // 对象内嵌数组
  "members": [                                    // 数组内嵌对象
    {
      "name": "张三",
      "scores": [ [90, 85], [92, 88] ]            // 数组内嵌数组
    }
  ]
}
```
### 数据访问
与c语言中的结构体类似。不过在Python中，访问JSON 解析后的对象（键值对）必须使用 `[]`
```python
# 假设变量名为data
print(data["studio_name"])
# QG

print(data["members"][0]["scores"][1])
# [92, 88]
```
---
## json库常用方法
json文本实质上是一条字符串，在程序中使用json数据需要特定方法**转换为对象变量使用**

| **方法**             | **操作对象** | **描述**                           |
| ------------------ | -------- | -------------------------------- |
| **`json.dumps()`** | **字符串**  | 将 Python 对象编码成 **JSON 字符串**      |
| **`json.loads()`** | **字符串**  | 将 JSON **字符串**解码为 Python 对象      |
| **`json.dump()`**  | **文件**   | 将 Python 对象序列化并**写入文件**          |
| **`json.load()`**  | **文件**   | 读取**文件**中的 JSON 数据并转化为 Python 对象 |
|                    |          |                                  |
### json.dumps()
```python
data = {'name':'nanbei','age':18}
print(json.dumps(data))
# {"name": "nanbei", "age": 18}
```
### json.loads()
```python
data = {"name": "nanbei", "age": 18} # json数据
a = json.loads(data)
print(a)
# {'name':'nanbei','age':18}
```
### json.dump()
```python
data = {'name': 'nanbei', 'age': 18}
with open('data.json', 'w', encoding='utf-8') as f:
    # 将 data 直接写入 f 指向的文件
    json.dump(data, f, indent=4)
```
### json.load()
```python
with open('data.json', 'r', encoding='utf-8') as f:
    # 直接从文件对象中解析出 Python 对象
    new_data = json.load(f)
    print(new_data)
```