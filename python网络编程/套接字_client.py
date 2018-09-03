import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    data = input('write here:')
    sock.sendto(data.encode('utf-8'),('127.0.0.1',12345))

    data = sock.recvfrom(1024)[0]

    print('the data recefrom sever:',data.decode('utf-8'))
    pass