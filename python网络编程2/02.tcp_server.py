import socket


# 设置地址
host = ''
port = 8888

# 创建套接字
sock = socket.socket()

# 绑定地址
sock.bind((host, port))

# 设置请求的数量
# listen()里需要一个整数作为参数，这个值表示等待队列中最大的连接数量
sock.listen(2)

while True:
    # 表示套接字可以接受连接
    # accept() 返回一个元组，元组中有两个元素
    # (连接对象,请求地址)
    # 可以将连接对象，当成客户端的socket
    conn, address = sock.accept()
    while True:
        # 获取客户端发送的数据
        data = conn.recv(1024)

        if not data:
            # 关闭连接 关闭连接就是在做4次挥手
            conn.close()
            break

        print('收到客户端发送的数据:',data)

        # 为客户端返回数据
        conn.send(b'Hello Client')

