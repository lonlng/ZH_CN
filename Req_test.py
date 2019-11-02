import requests

r = requests.get('http://192.168.88.130/python3.8/')
print("文本编码", r.encoding)
print("响应状态", r.status_code)
print("字符串方式的响应体", r.text)

