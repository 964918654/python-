import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.bind(('127.0.0.1',12345))

print('link start')

data,address = sock.recvfrom(1024)

print('get msg:',data.decode('utf-8'),address)

sock.sendto(b'Oh, i see',address)