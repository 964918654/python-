import socket

socket = socket.socket()

socket.bind(('',8080))

# socket.listen(5)

# conn , address = socket.accept()

host = socket.getsockname('www.baidu.com')

socket.connect((host,80))

data = b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9,en;q=0.8\r\nCookie: Pycharm-6c17d40=9878e4e3-6e0b-4289-83b6-50d233d5203c\r\n\r\n'

socket.send(data)

while True:
    data = socket.recv(1024)
    if not data:
        break
    print(data)


# while True:
#     data = conn.recv(1024)
#     if not data:
#         conn.close()
#         break
#
#     print(data)
#
socket.close()