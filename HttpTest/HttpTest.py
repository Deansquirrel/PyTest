# coding=utf-8
import threading
import urllib.request
import urllib.parse
import time


def get_http_request(url="http://www.baidu.com"):
    try:
        f = urllib.request.urlopen(url)
    # except Exception as e:
    #     print(e)
    except:
        return "超时"
    return f.read().decode('utf-8')
    # print(f.read().decode('utf-8'))


def create_data_line():
    # 123.57.226.114:9049
    no1 = get_http_request("http://123.57.226.114:9049/Api/Number/GetSno?workerId=1&&prefix=CR")
    no2 = get_http_request("http://123.57.226.114:9049/Api/Number/GetSno?workerId=1&&prefix=CR")
    no3 = get_http_request("http://123.57.226.114:9049/Api/Number/GetId?workerId=1")
    return no1 + "," + no2 + "," + no3


def get_result(index):
    print(index + " - " + create_data_line())


def get_result_list(title, num):
    for num in range(num):
        print(title + " " + get_result(str(num)))


if __name__ == "__main__":
    start = time.time()
    threads = []
    for i in range(10):
        thread = threading.Thread(target=get_result_list, args=(str(i), 100))
        threads.append(thread)
    for t in threads:
        t.setDaemon(True)
        t.start()
        time.sleep(0.05)
    for t in threads:
        t.join()
    end = time.time()
    print("%s" % (start,))
    print("%s" % (end,))
    print(end - start)
