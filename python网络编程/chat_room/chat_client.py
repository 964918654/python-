# 聊天室的客户端
import socket
from threading import Thread
import time

# 创建socket对象
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 创建一个变量，保存服务器的地址
host = '192.168.13.35'
port = 12345

sock.connect((host, port))  # 将套接字和指定的套接字进行连接

# 获取用户的用户名
username = input("请输入你的用户名：")
# 为用户名添加一个标识
username = '#username:'+username

# 向服务器发送用户名
# send()会默认项connect的地址发送数据
sock.send(username.encode('utf-8'))



# 创建一个函数，用来向服务器发送数据
def send_msg():
    while True:
        # 获取客户端要发送的数据
        data = input('')
        # 将数据发送给服务器
        sock.sendto(data.encode('utf-8'), (host, port))


# 创建一个函数，用来接收数据
def recv_msg():
    # 由于接收和发送数据的两个函数是在两个线程中执行的，
    #   如果接收数据先执行，则会由于连接尚未建立而报错
    while True:
        # 接收服务器返回的数据
        data = sock.recvfrom(1024)[0]
        # 将数据输出
        print(data.decode('utf-8'))


if __name__ == '__main__':
    # 创建两个线程，用来收发数据
    send_thread = Thread(target=send_msg)
    recv_thread = Thread(target=recv_msg)

    send_thread.start()
    recv_thread.start()

    send_thread.join()
    recv_thread.join()

