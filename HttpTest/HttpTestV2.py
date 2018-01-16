# coding=utf-8
import threading
import urllib.request
import urllib.parse
import time
import queue
import os


def get_http_request(url="http://www.baidu.com"):
    # http = urllib3.PoolManager()
    # r = http.request('GET', url)
    # print(r.data)
    # # return "aaa"
    # return r.data
    try:
        f = urllib.request.urlopen(url)
    except: # Exception as e:
        # print(e)
        return ""
    return f.read().decode('utf-8')


def get_sno(server):
    return get_http_request(server + "/Api/Number/GetSno?workerId=1&&prefix=CR")


def get_id(server):
    return get_http_request(server + "/Api/Number/GetId?workerId=1")


def get_line(server):
    time.sleep(0.05)
    no1 = ""
    while no1 == "":
        no1 = get_sno(server)
        if no1 == "":
            time.sleep(5)
    time.sleep(0.05)
    no2 = ""
    while no2 == "":
        no2 = get_sno(server)
        if no2 == "":
            time.sleep(5)
    time.sleep(0.05)
    no3 = ""
    while no3 == "":
        no3 = get_id(server)
        if no3 == "":
            time.sleep(5)
    result = no1 + "," + no2 + "," + no3
    # result.replace("\"", "")
    result = result.replace("\"", "")
    return result


def write_queue(my_queue, server):
    while 1 > 0:
        my_queue.put(get_line(server))
        time.sleep(0.05)


def write_file(my_queue, num):
    counter = 0
    while counter < num:
        if not my_queue.empty():
            counter = counter + 1
            print(counter)
            txt_name = "codingWord.txt"
            f = open(txt_name, 'a')
            f.write(my_queue.get())
            f.write("\n")
        time.sleep(0.025)


# http://123.57.226.114:9049
# http://116.62.200.182:10001
if __name__ == "__main__":
    start = time.time()
    sno_server = "http://123.57.226.114:9049"
    thread_num = 20
    need_num = 1000

    q = queue.Queue(maxsize=thread_num)
    threads = []
    for i in range(thread_num):
        thread = threading.Thread(target=write_queue, args=(q, sno_server))
        threads.append(thread)
    thread_write = threading.Thread(target=write_file, args=(q, need_num))
    threads.append(thread_write)
    for t in threads:
        t.setDaemon(True)
        t.start()
    thread_write.join()

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

    # for i in range(10):
    #     print(str(i) + " - " + get_line(sno_server))
    #     time.sleep(0.05)
    end = time.time()
    print("用时(秒)：" + str(end - start))
    input("\n按下 Enter 键后退出。")
