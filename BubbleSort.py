import urllib.request

def run(ls):
    for i in range(len(ls)-1):
        for j in range(len(ls)-i-1):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
    return ls
a = [1,9,4,77,3]
b=run(a)
print(b)
headers = {'User-Agent': "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)"}

r = urllib.request.urlopen('http://www.baidu.com/')

print(r.read().decode('utf-8'))