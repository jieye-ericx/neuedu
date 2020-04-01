from matplotlib import pyplot as plt
import random

x = ['语文', '数学', '英语']
y1 = [random.randint(70, 101) for i in range(3)]
y2 = [random.randint(60, 101) for i in range(3)]
y3 = [random.randint(50, 101) for i in range(3)]

plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title("六年级三科均分折线图")
plt.xlabel("科目")
plt.ylabel("平均分")
plt.yticks(range(50, 101, 10))

plt.plot(
    x,
    y1,
    color='red',
    marker='o',
    label='class 1'
)
plt.plot(
    x,
    y2,
    color='blue',
    marker='s',
    label='class 2'
)
plt.plot(
    x,
    y3,
    color='yellow',
    marker='d',
    label='class 3'
)
plt.grid(alpha=0.5)
plt.legend()
plt.show()
