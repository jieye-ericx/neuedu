from matplotlib import pyplot as plt
import requests
import json
import random


class ProtrayBar:
    def __init__(self, countryName):
        self.url = "https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?country={}"

        self.headers = [
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"
            },
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2"
            },
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
            }
        ]
        self.data_list = []
        self.url = self.url.format(countryName)

    def get_data(self, url):
        header = self.headers[random.randint(0, len(self.headers) - 1)]
        response = requests.get(url=url, headers=header)
        return self.parse_data(response.content.decode())

    def parse_data(self, content):
        data_dict = json.loads(content)
        # {'ret': 0, 'info': '', 'data': [{'date': '01.28', 'confirm_add': 0, 'confirm': 5, 'heal': 0, 'dead': 0},...
        # print(data_dict)
        dataOfAllDates = data_dict["data"]
        # print(dataOfAllDates)
        dataOfToday = dataOfAllDates[len(dataOfAllDates) - 1]
        return dataOfToday

    def run(self):
        """爬虫程序启动"""
        return self.get_data(self.url)


if __name__ == '__main__':
    countries = ['美国', '西班牙', '韩国', '意大利', '英国']
    barObjs = []
    for item in countries:
        barObjs.append(ProtrayBar(item).run())
    print(barObjs)
    # 设置中文
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # # 设置fig
    plt.figure(figsize=(20, 8), dpi=80)

    confirms = []
    heals = []
    deads = []
    for item in barObjs:
        confirms.append(item['confirm'])
        heals.append(item['heal'])
        deads.append(item['dead'])

    # 设置bar的宽度
    bar_width = 0.05

    # x轴
    new_x_confirms = list(range(len(countries)))
    new_x_heals = [i + bar_width for i in new_x_confirms]
    new_x_deads = [i + bar_width * 2 for i in new_x_confirms]

    plt.bar(range(len(countries)), confirms, width=bar_width, label="确诊")
    plt.bar(new_x_heals, heals, width=bar_width, label="治愈")
    plt.bar(new_x_deads, deads, width=bar_width, label="死亡")

    # 调整刻度
    plt.xticks(new_x_heals, countries)
    plt.title(barObjs[0]["date"] + "美国,西班牙,韩国,意大利,英国确诊治愈死亡人数",
              fontsize='large', fontweight='bold')
    plt.legend()
    plt.grid()
    plt.savefig('Countries新型肺炎条形图')
    plt.show()
