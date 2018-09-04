import socket
from threading import Thread
from queue import Queue


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

# 创建一个队列的对象，用来存储connection对象
conn_queue = Queue()

# 获取连接对象（生成者）
def get_conn():
    '''
        获取连接对象
    '''
    while True:
        conn, address = sock.accept()
        # 将连接放入到队列中
        conn_queue.put(conn)


# 使用连接对象接收发送数据的（消费者）
def do_conn():
    '''
        接收发送信息的线程
    '''
    while True:
        # 获取connection
        conn = conn_queue.get()
        # 从conn中读取数据
        while True:
            data = conn.recv(1024)

            if not data:
                conn.close()
                break
            print('收到客户端发送的数据:', data)

            # 为客户端返回数据
            conn.send(b'Hello Client')


# 创建一个线程，用来获取连接
conn_thread = Thread(target=get_conn)
# 创建一个线程，用来处理数据
t1 = Thread(target=do_conn)
t2 = Thread(target=do_conn)

# 启动线程
conn_thread.start()
t1.start()
t2.start()

conn_thread.join()
t1.join()
t2.join()