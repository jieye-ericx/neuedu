import numpy as np

# 1. 创建数组
# 1.1 把一个list转换成ndarray
# n1 = np.array([1, 2, 3])
# print(n1)
# print(type(n1))

# 1.2 利用range函数
# n2 = np.array(range(1, 10))
# print(n2)
# print(type(n2))

# 1.3 利用arange函数创建ndarray
# n3 = np.arange(1, 10)
# print(n3)
# print(type(n3))


# ---------------------- 注意以上创建得都是1维得ndarray
# 创建n维的ndarray
# 2. 创建n维的数组
# 2.1 利用array()创建 可以传入ndmin这个缺省参数来指定ndarray的维度
n4 = np.array([1, 2, 3,[4]], ndmin=2)
print(n4)

# 查看ndarray的维度(秩)
# 返回的长度就是ndarray的维度
# print(n4.ndim)

# 查看ndarray的形状
# print(n1.shape)
# print(n4.shape)

# 利用shape来调整一个ndarray的形状
# n4.shape = (1, 3)
# print(n4)

# ----------- demo
# n5 = np.array([1, 2, 3, 4, 5, 6])
# print(n5)
# print(n5.ndim)
#
# # 更改n5的形状
# n5.shape = (2, 3)
# print(n5)
# ndarray的秩取决于形状（返回的元组的长度）
# print(n5.ndim)





