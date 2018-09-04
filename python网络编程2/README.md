# 复习

## 网络编程
    - 套接字（socket）
    - 套接字用来在网络中负责接收和传输数据
    - 要想在网络中传输数据，必须将客户端和服务器的套接字相连
    - 套接字使用：
        核心类：
            socket.socket
            - 语法：
                socket.socket(family=AF_INET, type=SOCK_STREAM)
                    - family 使用的ip协议的版本
                        AF_INET 默认值 ip4
                        AF_INET6 ip6

                    - type 数据传输的协议
                        SOCK_STREAM 默认值 使用TCP协议来交互数据
                        SOCK_DGRAM  使用UDP协议来交互数据

                - 创建tcp的socket
                    sock = socket.socket()
                - 创建udp的socket
                    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

        方法：
        socket.bind(address)
            - 将套接字绑定到指定地址
            - 地址由两部分组成(host,port)
                - host 主机名
                    - 可以是ip地址，也可以是一个主机名 127.0.0.1 localhost
                    - host 可以是一个 '' 如果是空串，它会映射本机的所有地址
                    - 00000000.00000000.00000000.00000000
                        11111111.11111111.11111111.11111111
                    - 0.0.0.0 - 255.255.255.255
                    - 23.34.45.56 => www.baidu.com
                    - 由于ip地址不方便记忆，所以设计了hostname，
                        我们通过将一个hostname和一个ip地址进行映射
                        我们可以直接通过hostname来访问指定的ip地址
                    - 在计算机中，也可以自己配置host
                        C:\Windows\System32\drivers\etc\hosts
                        - 可以通过hosts来影响本机的地址和ip的映射
                    - 当我们在网络中访问一个地址时，
                        比如 www.baidu.com
                            浏览器会首先向DNS服务器发送请求，请求dns解析地址
                                返回网站的ip地址
                            然后浏览器在向ip地址发送请求
                            sock.gethostbyname() 根据名字获取ip地址

                - port 端口号
                    - 端口号是虚拟出来，在计算机中并不存在的无理的端口
                    - 一个端口号在计算机中对应一个进程，通过端口号可以找到对应的进程
                    - 一个端口号，只能被一个进程监听
                       - http协议默认端口 80
                       - https协议的默认端口 443


        socket.listen([backlog])
            - 启动套接字，指定最大的等待连接的数量
            - 用于tcp连接

        socket.connect(address)
            连接指定地址的套接字
            - 在UDP下，主要指定向哪个地址发送数据
            - 在TCP下，会真正的创建连接

        socket.accept()
            接受连接请求，套接字必须绑定到一个地址并监听连接。返回一个对(client,address)
            client
                请求方套接字对象
            address
                绑定到另一端的套接字地址


        socket.close()
            关闭套接字


        socket.recv(bufsize[, flags])
            从一个套接字接收数据，bufsize读取数据的最大长度，返回数据


        socket.recvfrom(bufsize[, flags])
            从一个套接字接收数据，bufsize读取数据的最大长度，返回数据和发送方地址的元组

        socket.send(bytes[, flags])
            发送数据，必须已经通过connect连接过端口

        socket.sendto(bytes, address)
            直接向指定的地址发送数据