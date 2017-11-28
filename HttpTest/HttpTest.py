# coding=utf-8
import threading
import urllib.request
import urllib.parse
from time import ctime


def get_http_request(url="http://www.baidu.com"):
    f = urllib.request.urlopen(url)
    return f.read().decode('utf-8')
    # print(f.read().decode('utf-8'))


def create_data_line():
    no1 = get_http_request("http://123.57.226.114:9049/Api/Number/GetSno?workerId=1&&prefix=CR")
    no2 = get_http_request("http://123.57.226.114:9049/Api/Number/GetSno?workerId=1&&prefix=CR")
    no3 = get_http_request("http://123.57.226.114:9049/Api/Number/GetId?workerId=1")
    return no1 + "," + no2 + "," + no3


def get_result(index):
    print(index + " - " + create_data_line())


if __name__ == "__main__":
    print("%s" % (ctime()))
    threads = []
    for i in range(10):
        print(i)
        thread = threading.Thread(target=get_result, args=(str(i),))
        threads.append(thread)

    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    print("%s" % (ctime()))

    # threads = []
    # t1 = threading.Thread(target=music, args=("AAA",))
    # threads.append(t1)
    # t2 = threading.Thread(target=move, args=("BBB",))
    # threads.append(t2)
    # for t in threads:
    #     t.setDaemon(True)
    #     t.start()
    #     print(t)
    # print("123")
    # t.join()
    # print(t)
    # print("all over %s" % ctime())
    #
    #
    # data = []
    # for num in range(100):
    #     print(num)
    #     data.append(create_data_line())
    # # data.append("a")
    # # data.append("b")
    # # data.append("c")
    # # data.append("d")
    # with open('test.txt', 'w') as fw:
    #     for letter in data:
    #         fw.writelines(letter + '\n')
