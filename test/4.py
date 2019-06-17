import re

a = '<p>Text</p><p>Text1<img src="url1">Text2<img src="url2">Text3</p><p><img src="url"></p>'
r = re.findall(r'>([^<>]+?)<|img src="([^<>]+?)"', a)
b = list(map(lambda i: i[0] if i[0] else i[1], r))
print(b)
