import socket
import time

# 设置目标地址
ser_host = '127.0.0.1'
ser_port = 8888

# 创建socket
sock = socket.socket()

# 连接服务器 connect()在tcp中就是在执行三次握手
sock.connect((ser_host,ser_port))

# 向服务器发送数据了
for i in range(10):
    time.sleep(1)
    sock.send(f'Hello Server {i}'.encode('utf-8'))
    data = sock.recv(1024)
    print('客户端收到服务器的数据：', data)



sock.close()
