import threading
import queue
import requests
import re


class CrawlThread(threading.Thread):

    def __init__(self, new_thread_name, new_queue_url, new_queue_data):
        super(CrawlThread, self).__init__()
        self.thread_name = new_thread_name
        self.queue_url = new_queue_url
        self.queue_data = new_queue_data
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}

    def run(self):
        while True:
            try:
                print("%s is launching" % self.thread_name)
                page = self.queue_url.get(block=False)
                url = "https://www.pengfu.com/xiaohua_" + str(page) + ".html"
                r = requests.get(url, headers=self.headers)
                r.encoding = 'utf-8'
                html = r.text
                self.queue_data.put(html)
            except:
                print("%s is stopped" % self.thread_name)
                break


class ParseThread(threading.Thread):
    def __init__(self, new_thread_name, new_queue_data, new_file, new_lock):
        super(ParseThread, self).__init__()
        self.thread_name = new_thread_name
        self.queue_data = new_queue_data
        self.file = new_file
        self.lock = new_lock

    def run(self):
        while True:
            try:
                print("%s is launching" % self.thread_name)
                html = self.queue_data.get(block=False)
                self.parse(html)
            except:
                print("%s is stopped" % self.thread_name)
                break

    def parse(self, html):

        title_pattern = re.compile(r"<div class='bdsharebuttonbox clearfix social_group' title=(.*?) humorId=.*?>", re.S)
        body_pattern = re.compile(r'<div class="content-img clearfix pt10 relative">(.*?)</div>', re.S)
        label_pattern = re.compile(r'<\w+/?>')
        title_ls = title_pattern.findall(html)
        body_ls = body_pattern.findall(html)
        for index, item in enumerate(title_ls):
            body_child = body_ls[index].replace("\t", "").replace("\n", "")
            body = label_pattern.sub(" ", body_child)
            dict_item = {item: body}
            print(dict_item)
            with self.lock:
                self.file.write(str(dict_item) + "\n")


def main():
    lock = threading.Lock()
    file = open("555.txt", "a")
    queue_data = queue.Queue()
    queue_url = queue.Queue(50)
    for i in range(1, 51):
        queue_url.put(i)

    crawl_num = []
    crawl_list = ["crawl_url_01", "crawl_url_02", "crawl_url_03"]
    for crawl_name in crawl_list:
        crawl_thread = CrawlThread(crawl_name, queue_url, queue_data)
        crawl_thread.start()
        crawl_num.append(crawl_thread)
    for crawl_thread in crawl_num:
        crawl_thread.join()

    parse_num = []
    parse_list = ["parse_data_01", "parse_data_02", "parse_data_03"]
    for parse_name in parse_list:
        parse_thread = ParseThread(parse_name, queue_data, file, lock)
        parse_thread.start()
        parse_num.append(parse_thread)
    for parse_thread in parse_num:
        parse_thread.join()

    with lock:
        file.close()
        print("all done !")


if __name__ == "__main__":
    main()

    """
    data = item + ":" + body
            with self.lock:
                self.file.write(data)
    dict_item = {item: body}
            final = json.dumps(dict_item, ensure_ascii=False)
            print(dict_item)
            with self.lock:
                self.file.write(final + "\n")
    """