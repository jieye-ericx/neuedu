# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from .settings import *
# import scrapy
import os


class SpiderprojectPipeline(object):
    def process_item(self, item, spider):
        print("管道1------------------->")
        print(item)
        return item


class SpiderprojectPipeline2(object):
    def process_item(self, item, spider):
        print("管道2------------------->")
        print(item)
        return item


class BMWImagePipline(ImagesPipeline):

    def get_media_requests(self, item, info):
        print("-------------------------get_media_requests-------------------------")
        # for url in item["image_urls"]:
        #     print(scrapy.Request(url))
        #     yield scrapy.Request(url)

        request = super(BMWImagePipline, self).get_media_requests(item, info)
        for obj in request:
            obj.item = item
            # print(obj.item.get('image_urls'))
        return request

    # def file_path(self, request, response=None, info=None):
    #     """重写此方法,来自定义保存路径"""
    #     print("-----------file_path-------------------")
    #     path = super(BMWImagePipline, self).file_path(request, response, info)
    #     # 获取分类
    #     category = request.item.get('category')
    #     # 获取最后的存储路径
    #     full_path = settings.IMAGES_STORE
    #     # 图片根据分类存储路径
    #     category_path = settings.os.path.join(full_path, category)
    #     # print(category_path)
    #     # 如果文件夹已经注册过了,就不创建了
    #     # 南工业/Spiderproject/images/分类的名称/当前分类下的所有的图片
    #     if not settings.os.path.exists(category_path):
    #         # 如果没有分类文件夹就创建该文件夹
    #         settings.os.mkdir(category_path)
    #         print("创建文件夹----ok!")
    #     # 图片名称
    #     img_name = path.replace("full/", "")
    #     # 生成最终的路径 + 图片名称
    #     return settings.os.path.join(category_path, img_name)


class DMPipeline(object):
    # def open_spider(self, spider):
    #     """在管道被启用的时候会被执行一次"""
    #     # 打开文件或者打开数据库连接
    #     # self.file = open("./")
    #     pass

    def process_item(self, item, spider):
        # 1. 先获取Book文件夹的路径
        book_store = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Book")
        # 2. 拼接小说目录
        fiction_path = os.path.join(book_store, item['fiction_name'])
        # 3. 判断小说的目录存在与否
        if not os.path.exists(fiction_path):
            # 如果没有分类文件夹就创建该文件夹
            print("----------创建文件夹----------")
            os.makedirs(fiction_path)
        # 小说章节
        fiction_store = os.path.join(fiction_path, "{}-{}".format(item['section'], item['section_name']))
        # 写入文件
        with open(fiction_store, 'w', encoding='utf-8') as f:
            # 写入文件
            f.write(item['section_content'])
        return item

    def close_spider(self, spider):
        """在管道关闭的时候会被执行一次"""
        # 关闭数据库 关闭文件流
        pass

