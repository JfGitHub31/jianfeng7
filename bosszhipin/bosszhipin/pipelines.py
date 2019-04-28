# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import pymysql


class BosszhipinPipeline(object):

    def process_item(self, item, spider):
        try:
            skill = item['skill']
            skill = ''.join(skill).replace("\n", "").replace(" ", "")  # final skill
            nature = item['nature'][0]  # final nature
            company = item['company']  # final company
            salary = item['salary'][-1]  # final salary
            job = item['job'][0]  # final job
            exp = item['exp'][0]
            exp_ls = re.findall(r'<p>(.*?)<em class="vline"></em>(.*?)<em class="vline"></em>(.*?)</p>', exp)
            city = exp_ls[0][0]  # final city
            exp = exp_ls[0][1]  # final exp
            edu = exp_ls[0][2]  # final edu

            params = (skill, nature, company, salary, job, city, exp, edu)
            connect = pymysql.connect(
                                        user="root",
                                        password="zjf123456",
                                        port=3306,
                                        host="127.0.0.1",
                                        charset="utf8",
                                        db="spiderdatabase"
                                                            )
            conn = connect.cursor()
            sql = "insert into bosszhipin(skill, nature, company, salary, job, city, exp, edu) values(%s, %s, %s, %s, %s, %s, %s, %s)"
            conn.execute(sql, params)
            connect.commit()
            print("done !!")
        except Exception as e:
            print(e)

        return item
