# coding=utf-8
import threading
import urllib.request
import urllib.parse
import time
import urllib3
import queue


def get_http_request(url="http://www.baidu.com"):
    # http = urllib3.PoolManager()
    # r = http.request('GET', url)
    # print(r.data)
    # # return "aaa"
    # return r.data
    try:
        f = urllib.request.urlopen(url)
    except Exception as e:
        print(e)
        return ""
    return f.read().decode('utf-8')


# http://123.57.226.114:9049
def get_sno(server):
    return get_http_request(server + "/Api/Number/GetSno?workerId=1&&prefix=CR")


def get_id(server):
    return get_http_request(server + "/Api/Number/GetId?workerId=1")


# def get_line(server, num):
#     for r_num in range(num):
#         no1 = get_sno(server)
#         no2 = get_sno(server)
#         no3 = get_id(server)
#         if no1 == "" or no2 == "" or no3 == "":
#             print("wait 5 seconds")
#             time.sleep(5)
#         else:
#             print(no1 + "," + no2 + "," + no3)


# def get_some_sno(server, num):
#     for r_num in range(num):
#         print(get_sno(server))
#
#
# def get_some_id(server, num):
#     for r_num in range(num):
#         print(get_id(server))
#
#
# def write_line(str_line):
#     print(str_line)
#
#
# def get_lines(line_num):
#     pass


if __name__ == "__main__":
    start = time.time()
    sno_server = "http://116.62.200.182:10001"

    # get_line(sno_server,10)


    # # 需求数量
    # total_num = 1
    # # 线程数量
    # thread_num = 1
    # # 每个线程需生成的数量
    # thread_create_num = int(total_num / thread_num)
    # if (total_num % thread_num) > 0:
    #     thread_create_num = thread_create_num + 1
    #
    # threads = []
    # # for i in range(10):
    # #     thread = threading.Thread(target=get_result_list, args=(str(i), 100))
    # #     threads.append(thread)
    # for i in range(thread_num):
    #     thread = threading.Thread(target=get_line, args=(sno_server, thread_create_num))
    #     threads.append(thread)
    # for t in threads:
    #     t.setDaemon(True)
    #     t.start()
    #     time.sleep(0.05)
    #
    # for t in threads:
    #     t.join()
    # end = time.time()
    # # print("%s" % (start,))
    # # print("%s" % (end,))
    # print(end - start)
