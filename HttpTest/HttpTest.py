import urllib.request
import urllib.parse


def get_http_request(url="http://www.baidu.com"):
    f = urllib.request.urlopen(url)
    return f.read().decode('utf-8')
    print(f.read().decode('utf-8'))


def create_data_line():
    no1 = get_http_request("http://123.57.226.114:9049/Api/Number/GetSno?workerId=1&&prefix=CR")
    no2 = get_http_request("http://123.57.226.114:9049/Api/Number/GetSno?workerId=1&&prefix=CR")
    no3 = get_http_request("http://123.57.226.114:9049/Api/Number/GetId?workerId=1")
    return no1 + "," + no2 + "," + no3


if __name__ == "__main__":
    data = []
    for num in range(100):
        print(num)
        data.append(create_data_line())
    # data.append("a")
    # data.append("b")
    # data.append("c")
    # data.append("d")
    with open('test.txt', 'w') as fw:
        for letter in data:
            fw.writelines(letter + '\n')



