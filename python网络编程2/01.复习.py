import socket

url = 'www.python.com' # 199.59.88.81
url = 'www.baidu.com' # 119.75.213.61
ip_address = socket.gethostbyname(url)
print(ip_address)