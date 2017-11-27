import urllib.request
import urllib.parse


def get_http_request(url = "http://www.baidu.com"):
    f = urllib.request.urlopen(url)
    return f.read().decode('utf-8')
    print(f.read().decode('utf-8'))


def test():
    no1 = get_http_request("http://123.57.226.114:9049/Api/Number/GetSno?workerId=1&&prefix=CR")
    no2 = get_http_request("http://123.57.226.114:9049/Api/Number/GetSno?workerId=1&&prefix=CR")
    no3 = get_http_request("http://123.57.226.114:9049/Api/Number/GetId?workerId=1")
    # print(no1 + "," + no2 + "," + no3)


if __name__ == "__main__":
    i = 0
    while i < 100:
        test()
        i = i + 1
