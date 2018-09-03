#创建一个客户端的socket
import socket

#创建一个socket对象
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 一般情况下客户端的socket不需要绑定地址和端口号，一般由系统自动分配
# 直接调用sock，向服务器发送数据
# sendto()用来向指定的地址发送数据
#   data 要发送的数据(二进制)
#   address 发送数据的地址
while True:
    #创建一个数据
    data = input('write here:')
    sock.sendto(data.encode('utf-8'),('127.0.0.1',12345))

    # 接受服务器返回的信息
    data = sock.recvfrom(1024)[0]

    print('the data recefrom sever:',data.decode('utf-8'))
    
    pass