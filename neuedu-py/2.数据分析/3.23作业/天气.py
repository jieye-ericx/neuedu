# 南京 2月份最高气温
# 南京 3月分最高气温
from matplotlib import pyplot as plt
import requests
import re
# 先爬取数据html
url = 'https://www.tianqi.com/nanjing/30/'
header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }
htmldata = requests.get(url=url, headers=header).content.decode()
# 拿到网页后，分析出需要的数据格式如下
# <div class="table_day ">
#   <a href="/tianqi/nanjing/20200328.html?qd=tq30" title="南京2020年03月28日天气">
#       <h3><b>03月28日</b> 星期六</h3>
#       <ul>
#          <li class="img"><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b1.png" /></li>
#          <li class="temp">多云 6~<b>13</b>℃</li>
#          <li>东风 2级</li>
#       </ul>
#   </a>
# </div>
pattern='<div class="table_day.*?">.*?<b>(.*?)</b>.*?class="temp">.*? (.*?)~<b>(.*?)</b>.*?</div>'
# 获得了对应日期温度的数组
normalizeddata =re.compile(pattern,re.S).findall(htmldata)
# 画图--------------------------------------------
plt.rcParams["font.sans-serif"] = ['SimHei']
plt.figure(figsize=(20, 8), dpi=80)

# 将数据分组存入对应数组
xLabelNames = []
minTe=[]# 最低温度
maxTe=[]
for item in normalizeddata:
    xLabelNames.append(item[0])
    minTe.append(int(item[1]))
    maxTe.append(int(item[2]))

# # 准备刻度轴
xLayoutLen = range(1, xLabelNames.__len__()+1)

# 绘制散点
plt.scatter(xLayoutLen, maxTe, label="最高气温分布")
plt.scatter(xLayoutLen, minTe, label="最低气温分布")

# 调整x以及y轴刻度数据
plt.xticks(xLayoutLen, xLabelNames, rotation=45)
plt.yticks(range(min(minTe), max(maxTe) + 1))

# ------------ figure 设置相关
plt.xlabel("时间(月份)")
plt.ylabel("温度")
plt.title("最高/低温度随月份变化散点图")
plt.grid(alpha=0.4)
plt.legend()
plt.savefig("./wea.png")
plt.show()
