# 1.冒泡排序
ls = [44, 6, 7, 99, 11, 34, 9,99,0]

for i in range(0, len(ls)):
    for i in range(len(ls) - 1):
        if ls[i] > ls[i+1]:
            ls[i],ls[i+1] = ls[i+1], ls[i]

print(ls)

# 2.python数据类型: 可变list 删除,dict 删除del dict["name"] 不可变set, tuple


# 3.闭包 一个函数内部又定义了一个函数
"""
def fun1(m):
    n = 1

    def fun2():

        print(n + m)

    return fun2


a=fun1(5)
a()
"""


# 装饰器及其功能
"""
引入日志
函数执行时间统计
执行函数前预备处理
执行函数后清理功能
权限校验等场景
缓存

def w1(func):

    def inner():
        # 验证1
        # 验证2
        # 验证3
        print("验证")
        func()
    return inner

@w1
def f1():
    print('f1')

f1()


def makeBold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

@makeBold
def test1():
    return "hello world-1"


print(test1())
"""



# numpy和pandas的作用
"""
numpy支持维度数组和矩阵运算
numpy.array()生成数组,其中dtype可以指定类型
numpy.arange(6)生成连续元素[0,1,2,3,4,5,6]

pandas的主要数据结构:Series和DataFrame
Series是一种类似于一维数组对象且支持index
DataFrame是一个类似表个性的数据结构
常用添加列的方式  df=DataFrame({"scorename": name_list})
               df[score] = score_list[i]
如果score列不存在则会一列一列的往右添加

"""

# tcp
"""
tcp三次握手
1.client端发送一个syn数据类型和一个0的序号到server端
2.server此时发送syn+ack的数据类型和一个为1的序号到client,告诉client我一准备好了,你准备好了吗
3.client此时发送ack和一个为1的序号到server端,告诉server我也准备好了.到此connect建立了

tcp四次挥手
1.假设client首先调用close()并发送fin的数据类型给server,告诉server我要关闭连接了.
2.server此时发送ack给client,告知我已收到确认
3.server此时调用close()并发送fin给client,告诉client我也要关闭连接了.
4.client此时发送ack给server,我也知道了.到此connect断开
"""

# tcp和udp的区别
"""
tcp稳定,因为在tcp中如果一方收到对方的数据一定发送ack给对方,而在udp中没有这个过程.
"""

# http和https
"""
1.https协议需要到ca申请证书，一般免费证书较少，因而需要一定费用。

2.http是超文本传输协议，信息是明文传输，https则是具有安全性的ssl加密传输协议。

3.http和https使用的是完全不同的连接方式，用的端口也不一样，前者是80，后者是443。

4.http的连接很简单，是无状态的；HTTPS协议是由SSL+HTTP协议构建的可进行加密传输、身份认证的网络协议，比http协议安全。
"""

# 线程,进程,携程
"""
进程:进程就是一个程序的一次动态执行过程,一般有程序,数据集,进程控制块三部分组成
线程:线程旨在一个进程中提高系统的并发性


"""


# mysql和mongodb
"""
mongodb非关系型数据库即文档类型数据库
存储方式：虚拟内存+持久化存储
缺点:没有事务机制

mysql
存储方式:硬盘存储
缺点:海量数据存储效率变慢
引擎:InnoDB, Mylsam, Memory

"""

# redis 开源的key-value内存数据库
"""
redis数据结构:string, map, list, sets等
优点:速度快,持久化,自动操作
缺点:收内存限制不能用作海量数据的高性能读写
"""

# cookie和session的区别
"""
session:session存在服务端,且实现会话保持,更安全
cookie:cookie存在客户端,也可以会话保持,但很不安全
"""

# 网络传输——-http在哪一层
"""
数据链路层
网络层
传输层
应用层 -- http所在层
"""

# celery
"""
Celery 是一个简单、灵活且可靠的，处理大量消息的分布式系统，并且提供维护这样一个系统的必需工具
"""


# uwsgi
"""
uWSGI:是一种web服务器
"""


# 类
"""
class All():

    def __init__(self, name):
        self.name = name


class Animal(All):
    def __init__(self,name, age):
        super().__init__(name)
        self.age=age
        pass


    def pri(self):
        print("名字为%s,age为%d"%(self.name, self.age))



def mypri(animal):
    animal.pri()

a = Animal('小黄', 30)

mypri(a)



class Car():
    def __init__(self):
        self.wheelNum = 4
        self.color = '蓝色'

    def move(self):
        print('车在跑,目标夏威夷')

    # 创建对象
BMW = Car()
Bench = Car()
print('车的颜色为:%s'%(BMW.color))
print('车的颜色为:%s'%(Bench.color))

class Car():

    def __init__(self, newWheelNum, newColor):
        self.wheelNum = newWheelNum
        self.color = newColor

    def __str__(self):
        msg = "嘿。。。我的颜色是" + self.color + "我有" + str(self.wheelNum) + "个轮胎..."
        return msg

    def move(self):
        print('车在跑，目标:夏威夷')


BMW = Car(4, "白色")
print(BMW)
"""

# python django orm

"""
orm对象关系映射
1.根据对象的类型生成表结构
2.将对象,列表的操作,转换为sql语句
3.将sql语句转化为对象,列表

`ForeignKey`：一对多，将字段定义在多的端中
`ManyToManyField`：多对多，将字段定义在两端中
`OneToOneField`：一对一，将字段定义在任意一端中

用一访问多：对象.模型类小写_set
bookinfo.heroinfo_set

用一访问一：对象.模型类小写
heroinfo.bookinfo

访问id：对象.属性_id（mysql中的表属性名为:属性_id）
heroinfo.book_id
"""


# python3中的zip

"""
a1 = [1,2,3]
a2 = [4,5,6]

a = zip(a1, a2)
print(dict(a), type(a))

b1 = {"a":"1", "b":"2"}
b2 = {"c":"3", "d":"4"}

print(dict(zip(b1,b2)))
"""



# python3中的map
#
# l1 = [ 0, 1, 2, 3, 4, 5, 6 ]
# l2 = [ 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat' ]
# aa = list(map(str, l1))
#
# print(aa,type(aa))




# python3中的reduce

"""
from functools import reduce

def add(x,y):
    print(x,y)
    return x + y

print(reduce(add, (1,2,4)))


print(reduce(lambda x,y: x+y, [1,2,3,4]))
"""



import re

a = '<p>Text</p><p>Text1<img src="url1">Text2<img src="url2">Text3</p><p><img src="url"></p>'

r = re.findall(r'>([^<>]+?)<|img src="([^<>]+?)"', a)
b = list(map(lambda i: i[0] if i[0] else i[1], r))
print(b)