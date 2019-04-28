# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class DdangPipeline(object):

    def process_item(self, item, spider):
        for index, title in enumerate(item['title']):
            try:
                title = title
                price = item["price"][index][1:]
                publish = item["publish"][index]
                comment = item["comment"][index]
                link = item["link"][index]

                params = (title, price, publish, comment, link)
                connect = pymysql.connect(
                                          user="root",
                                          password="****",
                                          port=3306,
                                          host="127.0.0.1",
                                          db="ddang",
                                          charset="utf8"
                                                        )
                conn = connect.cursor()
                sql = "insert into ddang(title, price, publish, comment, link) values(%s, %s, %s, %s, %s)"
                conn.execute(sql, params)
                connect.commit()
                print("done !!")
            except Exception as e:
                print(e)
        return item
