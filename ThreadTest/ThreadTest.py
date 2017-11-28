# coding=utf-8
import threading
from time import ctime,sleep

# https://www.cnblogs.com/fnng/p/3670789.html


def music(func):
    for i in range(2):
        print("I was listening to music %s. %s" % (func, ctime()))
        sleep(1)


def move(func):
    for i in range(2):
        print("I was at the %s! %s" % (func, ctime()))
        sleep(5)


if __name__ == '__main__':
    music('AAA')
    move('BBB')
    print("all over %s" % ctime())