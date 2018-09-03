# 聊天室的服务器
import socket

# 创建两个变量，表示服务器的地址
host = '192.168.13.35'  # host表示主机名
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
#       2、压根不知道谁是谁
#       3、客户端之间不能沟通
#       4、服务器不能决定给谁发消息
#
#

# 创建一个字典用来保存用户的数据
user_dict = {}

print('聊天室已经启动，大家来聊天吧...')

while True:
    # 接收数据
    try:
        data, address = sock.recvfrom(1024)
    except:
        continue
    # 检查用户发送的数据是否是用户名
    data = data.decode('utf-8')

    if data.startswith('#username:'):
        # 是用户名
        # 去掉字符串中 #username
        username = data.split(':', 1)[1]
        # print(f'{username}上线了~~~')
        # 将用户信息存储到字典中{key:value}
        # key是客户端的地址，value是用户名
        # print(address)
        user_dict[address] = username
        msg = f'{username}上线了~~~'
        msg = msg.encode('utf-8')

        # 通知每一个用户，有新用户上线了
        # 遍历用户的字典
        for user_add in user_dict.keys():
            sock.sendto(msg, user_add)

        # print(user_dict)

        continue

    # 如果用户输入的不是用户名，则需要将信息发送给每一个用户
    data = user_dict[address]+' : '+data
    data = data.encode('utf-8')

    for user_add in user_dict.keys():
        sock.sendto(data, user_add)

    # 打印数据
    # print(data)
    # 发送数据(服务器向客户端返回数据)
    # 获取输入
    # msg = input('请输入一个信息：')
    # msg = 'hello'
    # sock.sendto(msg.encode('utf-8'), address)
