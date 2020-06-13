# -*- coding: utf-8 -*-
import scrapy
from ..items import DMItem


class DmSpider(scrapy.Spider):
    name = 'DM'
    allowed_domains = ['daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    def parse(self, response):
        # print(response.status)
        # 创建item(一部小说)
        # item = DMItem()

        # print(response.body.decode())
        # 获取所有小说的章节详情连接(不包括最后两部的沙海和藏海花)
        a_links = response.xpath('//ul[@class="sub-menu"]/li/a/@href').getall()
        # 处理最后两部小说
        for x in response.xpath('//div[@class="sitenav"]/ul/li/a/@href')[1:].getall():
            a_links.append(x)

        for link in a_links:
            yield scrapy.Request(
                url=link,
                callback=self.parse_section_list_page
            )

    def parse_section_list_page(self, response):
        # print("来到了章节列表页面--------------")
        # 解析数据
        # print(response.body.decode())
        # print("----------------------------------")
        arcticle_node = response.xpath('//article')

        for arcticle in arcticle_node:
            item = DMItem()
            # 保存
            fiction_list = arcticle.xpath('./a/text()').get().split()

            if len(fiction_list) == 3:
                item['fiction_name'] = fiction_list[0]
                item['section'] = fiction_list[1]
                item['section_name'] = fiction_list[2]
            else:
                item['fiction_name'] = fiction_list[0]
                item['section'] = fiction_list[1]
                item['section_name'] = ''
            # 获取章节详情的地址(内容)
            item['section_link'] = arcticle.xpath('./a/@href').get()

            yield scrapy.Request(
                url=item['section_link'],
                callback=self.parse_fiction_content,
                method='GET',
                meta={
                    "key": item
                }
            )

    def parse_fiction_content(self, response):
        # response.body
        # response.status
        # 取传递过来item
        item = response.meta.get("key")

        # 获取小说内容
        content = response.xpath('//article[@class="article-content"]/p/text()').getall()

        # 解析小说内容
        item["section_content"] = '\n'.join(content)
        # print(item["section_content"])
        # print("---------------------------------")
        # 发送给管道
        yield item







