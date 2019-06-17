import sys
import pymysql
import configparser
import pandas as pd
from pandas import HDFStore
from sqlalchemy import create_engine


# def select_server():
#     dt = {}
#     server = sys.argv[1]
#     conf = configparser.ConfigParser()
#     conf.read("config.ini", encoding="utf8")
#     sections = conf.sections()
#
#     if server in sections:
#         ls = conf.items(sections[0])
#         for i in ls:
#
#             dt[i[0]] = i[1]
#
#     return dt


def connect(flag):
    # dt = select_server()
    conn = pymysql.connect(
        host="localhost",
        user="root",
        passwd="123",
        charset='utf8',
        port=3306,
        db="zzjz_web_test"
    )
    if flag == 0:
        return conn.cursor()
    elif conn == "":
        return conn
    else:
        return ""


def connect_bp():
    # dt = select_server()
    engine = create_engine('mysql+pymysql://root:123@localhost:3306/zzjz_web_test')
    return engine


def fetch_sql(sql):
    cur = connect(0)
    cur.execute(sql)

    return cur.fetchall()


def select_table(table_name):
    table_ls = []
    conn = connect(0)
    table_tup = fetch_sql("show tables")

    for item in table_tup:
        table_ls.append(item[0])
    # print(table_ls)

    if table_name in table_ls:
        return 0
    return 1


def read_table_p():
    df_ls = []
    engine = connect_bp()
    table_name = "t_component"
    # table_name = "nodefile"
    sql = "select count(*) from %s" % table_name
    length = fetch_sql(sql)[0][0]

    if select_table(table_name) == 0:

        for count in range(2):
            sql = "select * from %s limit %d, 1" % (table_name, count)

            df = pd.read_sql(sql, engine)
            print(df)
            df.to_csv(df["ID"][count]+".csv")

            # df.to_excel(excel_writer=excelWriter, sheet_name="info1", index=None)
            # sh = "sheet%d" % count
            # writer = pd.ExcelWriter("%s.xls" % df["ID"][count])
            #
            # df.to_excel(excel_writer=writer, sheet_name=sh)
            #
            # writer.save()



read_table_p()



"""
https://blog.csdn.net/OnePiece_97/article/details/88659057  mysql
"""