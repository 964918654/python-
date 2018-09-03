# 编写一个简易的服务器
import socket

# 创建两个变量，表示服务器的地址
host = '127.0.0.1'  # host表示主机名
port = 12345  # port表示端口号

# 创建socket对象
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定地址
sock.bind((host, port))

# 服务器的主要逻辑的代码（接收和发送数据）都要写在一个死循环中
# 因为一般情况下，服务器是不能停止的
# 简易的聊天程序：
#   问题：
#       1、收到消息才能回复，回复完才能接收
#       2、服务器不能决定给谁发消息
#       3、客户端之间不同沟通
#       4、压根不知道谁是谁

print('聊天室已经启动，大家来聊天吧...')

while True:
    # 接收数据
    data, address = sock.recvfrom(1024)
    # 打印数据
    print('收到数据：', data.decode('utf-8'))
    # 发送数据(服务器向客户端返回数据)
    # 获取输入
    msg = input('请输入一个信息：')
    sock.sendto(msg.encode('utf-8'), address)
    