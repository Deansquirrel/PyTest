# coding=utf-8
import threading
from time import ctime,sleep

# https://www.cnblogs.com/fnng/p/3670789.html


def music(func):
    for i in range(2):
        print("I was listening to music %s. %s" % (func, ctime()))
        sleep(2)


def move(func):
    for i in range(2):
        print("I was at the %s! %s" % (func, ctime()))
        sleep(1)


if __name__ == '__main__':
    threads = []
    t1 = threading.Thread(target=music, args=("AAA",))
    threads.append(t1)
    t2 = threading.Thread(target=move, args=("BBB",))
    threads.append(t2)
    for t in threads:
        t.setDaemon(True)
        t.start()
        print(t)
    print("123")
    t.join()
    print(t)
    print("all over %s" % ctime())