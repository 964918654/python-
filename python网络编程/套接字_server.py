#通过socket模块来操作套接字
# from socket import socket
import socket
#通过socket来创建套接字对象
#socket需要两个参数：
#1.指定ip协议版本 默认值 AF_INET 表示使用 IPv4版本 192.168.xxx.xxx
#        AF_INET6 表示IPv6版本，这个东西目前用的比较少
#2.指定套接字的类型：
#   流套接字，socket.SOCK_STREAM,默认值，表示使用TCP协议
#   数据报套接字，socket.SOCK_DGRAM 表示UDP协议
#   TCP协议：安全的协议（不会丢失数据），一般使用TCP协议
#   UDP协议：不安全（有可能丢失数据）

#创建一个sock对象，使用ipv4和UDP协议来处理数据
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#sock = socket.socket(type = socket.SOCK_DGRAM)
#sock对象分成两种，一种是服务器的socket 一种客户端的socket
#创建的是服务器的socket，则必须为服务器指定一个固定的地址
#   一个服务器的地址由两部分组成，ip地址和端口号
#socket.bind(address)用来将一个套接字对象和一个地址绑定
# - address，服务器的地址，它是一个元组
#       （'ip地址'，端口号）

#ip地址是计算机在网络中的唯一的地址，在网络中通过ip地址来识别计算机
#127.0.0.1表示本机
sock.bind(('127.0.0.1',12345))

print('link start')

#接受客户端发送的数据
#recvfrom（）从其他的套接字处，接受数据
#   需要一个参数，指定接收数据的最大长度单位字节
#       - 返回一个元组，元组中有两个元素
#       - 1.客户端发送的数据
#       - 2.客户端（发送方）的地址
# recvfrom()调用以后，直到有数据发送，代码才会向下执行，否则会一直阻塞

data,address = sock.recvfrom(1024)  # 接收数据，最大接收1kb的数据

print('get msg:',data.decode('utf-8'),address)

# 通过服务器向客户端返回数据
sock.sendto(b'Oh, i see',address)