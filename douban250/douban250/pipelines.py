# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class Douban250Pipeline(object):

    def process_item(self, item, spider):
        try:
            title = item['title'][0]
            director = item['director'][0]
            type = item['type'][0]
            date = item['date'][0]
            time_long = item['time_long'][0]
            comment = item['comment'][0]
            score = item['score'][0]
            link = item['link']


            params = (title, director, type, date, time_long, comment, score, link)
            connect = pymysql.connect(
                                        user="root",
                                        password="zjf123456",
                                        port=3306,
                                        db="spiderdatabase",
                                        host="127.0.0.1",
                                        charset="utf8"
                                                        )

            conn = connect.cursor()
            sql = "insert into douban250(title, director, type, date, time_long, comment, score, link) values(%s, %s, %s, %s, %s, %s, %s, %s)"
            conn.execute(sql, params)
            connect.commit()
            print("done !!")
        except Exception as e:
             print(e)

        return item

