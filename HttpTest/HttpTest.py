# coding=utf-8
import threading
import urllib.request
import urllib.parse
import time


def get_http_request(url="http://www.baidu.com"):
    try:
        f = urllib.request.urlopen(url)
    except:# Exception as e:
        # print(e)
        return "超时"
    return f.read().decode('utf-8')
    # print(f.read().decode('utf-8'))


def create_data_line():
    # 123.57.226.114:9049
    no1 = get_http_request("http://106.14.57.245:10001/Api/Number/GetSno?workerId=1&&prefix=CR")
    no2 = get_http_request("http://106.14.57.245:10001/Api/Number/GetSno?workerId=1&&prefix=CR")
    no3 = get_http_request("http://106.14.57.245:10001/Api/Number/GetId?workerId=1")
    return no1 + "," + no2 + "," + no3


def get_result(index):
    print(index + " - " + create_data_line())


if __name__ == "__main__":
    start = time.time()
    threads = []
    for i in range(1000):
        thread = threading.Thread(target=get_result, args=(str(i),))
        threads.append(thread)
    for t in threads:
        t.setDaemon(True)
        t.start()
        time.sleep(0.1)
    for t in threads:
        t.join()
    end = time.time()
    print("%s" % (start,))
    print("%s" % (end,))
    print(end - start)
