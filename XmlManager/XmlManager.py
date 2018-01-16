# coding=utf-8
import xml.dom.minidom

# 参考
# https://www.cnblogs.com/fnng/p/3581433.html
# API
# https://docs.python.org/2/library/xml.dom.html


def is_node_valid(node_name):
    return True


def get_node_value(node_name):
    return "nodeValue"


if __name__ == '__main__':
    print("--------------------------------------")
    print("Begin")
    print("--------------------------------------")

    dom = xml.dom.minidom.parse('Data\Web.config')
    # dom = xml.dom.minidom.parse('Data\ZLWebApiAppSetting.xml')
    root = dom.documentElement

    root = dom.documentElement

    print(root.nodeName)

    node = dom.getElementsByTagName(root.nodeName)
    print(node.length)
    if node.length > 1:
        print("多个根节点数量异常")
        exit()

    if node.length <1:
        print("无根节点")
        exit()

    for i in range(node.length):
        item = node.item(i)
        print(item.nodeName)
        sub_node = node.item(i).getElementsByTagName("appSettings")
        print(sub_node.length)
        for i in range(sub_node.length):
            item = sub_node.item(i)
            print(item.nodeName)

    # print(root.length)

    print("--------------------------------------")
    print("End")
    print("--------------------------------------")