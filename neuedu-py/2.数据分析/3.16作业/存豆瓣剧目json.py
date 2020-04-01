import requests
import json
import random

class DouBanTV:
    def __init__(self, class_name):
        self.class_name = class_name
        self.url = "https://movie.douban.com/j/search_subjects?type=tv&tag={}&sort=recommend&page_limit=20&page_start={}"
        self.headers = [
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/79.0.3945.130 Safari/537.36 "
            }, {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"
            }, {
                "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) "
                              "Version/5.1 Safari/534.50 "
            },
        ]
        self.data_list = []
        self.urls = [self.url.format(self.class_name, i * 20) for i in range(10)]

    def get_data(self, url):
        header = self.headers[random.randint(0, len(self.headers) - 1)]
        response = requests.get(url=url, headers=header)
        self.parse_data(response.content.decode())

    def parse_data(self, content):
        data_dict = json.loads(content)
        for tv_info in data_dict["subjects"]:
            tv_dict = {"tv_title": tv_info["title"], "tv_rate": tv_info["rate"], "tv_url": tv_info["url"]}
            self.data_list.append(tv_dict)
        return self.data_list

    def save_data(self, data):
        path = "./tv_" + self.class_name + ".json"
        with open(path, "a", encoding="utf-8") as f:
            print(data)
            # for content in data:
            #     f.write(json.dumps(content, ensure_ascii=False, indent=4))
            #     f.write("\n")
            # 直接把json对象存为json文件
            f.write(json.dumps(data))
            f.close()

    def run(self):
        for url in self.urls:
            print(url)
            self.get_data(url)
        self.save_data(self.data_list)


if __name__ == '__main__':
    classes = ["美剧", "日剧", "韩剧", "日本动画", "纪录片"]
    for i in range(len(classes)):
        print(i, "-------", classes[i])
    id = int(input("输入对应剧目序号："))
    DouBanTV(classes[id]).run()
    print("已存入同目录json文件！")
