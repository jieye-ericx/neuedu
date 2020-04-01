from matplotlib import pyplot as plt
# Matplotlib是Python的绘图库，其中的pyplot包封装了很多画图的函数。

# Matplotlib.pyplot 包含一系列类似 MATLAB 中绘图函数的相关函数。
# 每个 Matplotlib.pyplot 中的函数会对当前的图像进行一些修改，
# 例如：产生新的图像，在图像中产生新的绘图区域，在绘图区域中画线，
# 给绘图加上标记，等等…… Matplotlib.pyplot 会自动记住当前的图像和绘图区域，
# 因此这些函数会直接作用在当前的图像上。

# pyplot库, 包含所有得绘制图形的函数


# 1. 图片的设置
plt.figure(figsize=(40, 82), dpi=80)

# 2. 准备刻度 x轴数据以及y轴数据 一点包含(x1, y1)
# x轴数据必须和y轴数据的数量得一致
# for x in range(1, 10, 2):
#     print(x)
x = range(1, 10, 2)
y = [20, 13, 12, 11, 2]

# 3. 设置x轴刻度
plt.xticks(range(1, 10))
plt.yticks(range(min(y), max(y)+1))

# 4. 绘制
plt.plot(x, y)

# 5. 显示图片
# plt.show()

# 6. 保存图片
plt.savefig("./01.png")


