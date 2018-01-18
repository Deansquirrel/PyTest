# coding=utf-8
import xml.dom.minidom

# API
# https://docs.python.org/3.6/library/xml.dom.html


# 根据path获取dom对象
def get_xml_dom(file_path):
    xml_str = ""
    try:
        file_object = open(file_path, encoding="utf-8")
        lines = file_object.readlines()
        for line in lines:
            line = line.strip()
            if line != "":
                xml_str = xml_str + line
    except Exception as err:
        print('错误信息：{0}'.format(err))
        exit()
    finally:
        file_object.close()
    return xml.dom.minidom.parseString(xml_str)


# 将dom对象写入文件
def write_xml_dom(file_path, document):
    try:
        with open(file_path, 'w', encoding='UTF-8') as fh:
            document.writexml(fh, indent="", addindent='  ', newl='\n', encoding='UTF-8')
    except Exception as err:
        print('错误信息：{0}'.format(err))


# 获取节点dom
def get_sub_dom(xml_dom, node_path, find_key, find_value):
    node_path_dict = node_path.split("|")
    this_node = node_path_dict.pop(0)
    if xml_dom:
        if xml_dom.hasChildNodes():
            child_nodes = xml_dom.childNodes
            for i in range(child_nodes.length):
                item = child_nodes.item(i)
                if item.nodeName == this_node:
                    # 找到当前节点
                    if len(node_path_dict) == 0:
                        if find_key == "":
                            return item
                        else:
                            if item.hasAttribute(find_key):
                                attr_value = item.getAttribute(find_key)
                                if attr_value == find_value:
                                    return item
                    else:
                        return get_sub_dom(item,'|'.join(node_path_dict),find_key,find_value)
        raise Exception("未找到节点 - 【" + this_node + "】【" + find_key + "】【" + find_value + "】")
        # print("未找到节点 - 【" + this_node + "】【" + find_key + "】【" + find_value + "】")


# 修改节点属性
def chang_attribute(xml_dom, node_path, check_key, check_value, change_key, change_value):
    sub_dom = get_sub_dom(xml_dom, node_path, check_key, check_value)
    if sub_dom:
        if sub_dom.hasAttribute(change_key):
            sub_dom.setAttribute(change_key, change_value)
        else:
            raise Exception("节点不存在属性 - 【" + change_key + "】")
            # print("节点不存在属性 - 【" + change_key + "】")


# 修改节点Text
def chang_text(xml_dom, node_path, check_key, check_value, new_text):
    sub_dom = get_sub_dom(xml_dom, node_path, check_key, check_value)
    if sub_dom:
        sub_dom.firstChild.data = new_text


if __name__ == '__main__':
    print("--------------------------------------")
    print("Begin")
    print("--------------------------------------")

    # file = "Data\Web.config"
    file = "Data\ZLWebApiAppSetting.xml"

    dom = get_xml_dom(file)

    try:
        # 属性修改举例
        chang_attribute(dom, "configuration|runtime|assemblyBinding",
                    "xmlns", "urn:schemas-microsoft-com:asm.v1",
                    "xmlns", "new xmlns value")
        # 文本修改举例
        chang_text(dom, "appSettings|RunLogLevel", "", "", "newText")
    except Exception as ex:
        print(ex)

    write_xml_dom(file, dom)

    print("--------------------------------------")
    print("End")
    print("--------------------------------------")