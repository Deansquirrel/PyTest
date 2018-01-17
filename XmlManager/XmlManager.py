# coding=utf-8
import xml.dom.minidom

# API
# https://docs.python.org/3.6/library/xml.dom.html


# 根据path获取dom对象
def get_xml_dom(path):
    xml_str = ""
    try:
        file_object = open(path, encoding="utf-8")
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
def write_xml_dom(path, document):
    try:
        with open(path, 'w', encoding='UTF-8') as fh:
            document.writexml(fh, indent="", addindent='\t', newl='\n', encoding='UTF-8')
    except Exception as err:
        print('错误信息：{0}'.format(err))


# 修改节点属性
def chang_attribute(att_path, check_key, check_value, change_key, change_value):
    pass


# 修改节点Text
def chang_text(att_path, check_key, check_value, new_text):
    pass


if __name__ == '__main__':
    print("--------------------------------------")
    print("Begin")
    print("--------------------------------------")

    file_path = "Data\Web.config"
    # path = "Data\ZLWebApiAppSetting.xml"

    dom = get_xml_dom(file_path)

    root = dom.documentElement
    app_settings = root.getElementsByTagName("appSettings")

    if app_settings.length < 1:
        print("无appSettings节点")
        exit()

    node_app_settings = app_settings.item(0)
    node_list_add = node_app_settings.getElementsByTagName("add")

    for i in range(node_list_add.length):
        node_add = node_list_add.item(i)
        if node_add.getAttribute("key") == "webpages:Version":
            print(node_add.getAttribute("value"))
            node_add.setAttribute("value", "3.0.0.0")
            print(node_add.getAttribute("value"))

    write_xml_dom(path, dom)

    print("--------------------------------------")
    print("End")
    print("--------------------------------------")