import socket

# host = ''
# port = 12345
#
# sock = socket.socket()
#
# sock.bind((host,port))
#
# sock.listen(5)
#
# conn,address = sock.accept()
#
# # 获取客户端发送的内容
# data = conn.recv(1024*64)
#
# # b'GET / HTTP/1.1\r\nHost: 127.0.0.1:12345\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nReferer: http://localhost:63342/course/day19/code/page/index.html\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9,en;q=0.8\r\n\r\n'
#
# print(data.decode('utf-8'))

sock = socket.socket()

# 连接baidu的服务器
host = socket.gethostbyname('news.baidu.com')
port = 80

sock.connect((host,port))

data = b'GET / HTTP/1.1\r\nHost: news.baidu.com\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nReferer: http://localhost:63342/course/day19/code/page/index.html\r\nAccept-Language: zh-CN,zh;q=0.9,en;q=0.8\r\n\r\n'

sock.send(data)

data = sock.recv(1024*1024)

# b'HTTP/1.1 200 OK\r\nConnection: keep-alive\r\nContent-Type: text/html;charset=utf-8\r\nDate: Tue, 04 Sep 2018 08:47:14 GMT\r\nP3p: CP=" OTI DSP COR IVA OUR IND COM "\r\nServer: Apache\r\nSet-Cookie: BAIDUID=D9C4990945B6FF5D182BD7DC9CFF6768:FG=1; expires=Wed, 04-Sep-19 08:47:14 GMT; max-age=31536000; path=/; domain=.baidu.com; version=1\r\nTracecode: 28349116390688931594090416\r\nTracecode: 28348769410785787402090416\r\nVary: Accept-Encoding\r\nVary: Accept-Encoding\r\nX-Bd-Api: news_index\r\nX-Bd-Status: 200\r\nTransfer-Encoding: chunked\r\n\r\n39a\r\n<!doctype html>\n<html class="expanded">\n<head>\n\n<!--STATUS OK-->\n<meta http-equiv=Content-Type content="text/html;charset=utf-8">\n<meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1">\n<link rel="icon" href="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/img/favicon.ico" mce_href="../static/img/favicon.ico" type="image/x-icon">\n\n<title>\xe7\x99\xbe\xe5\xba\xa6\xe6\x96\xb0\xe9\x97\xbb\xe2\x80\x94\xe2\x80\x94\xe5\x85\xa8\xe7\x90\x83\xe6\x9c\x80\xe5\xa4\xa7\xe7\x9a\x84\xe4\xb8\xad\xe6\x96\x87\xe6\x96\xb0\xe9\x97\xbb\xe5\xb9\xb3\xe5\x8f\xb0</title>\n<meta name="description" content="\xe7\x99\xbe\xe5\xba\xa6\xe6\x96\xb0\xe9\x97\xbb\xe6\x98\xaf\xe5\x8c\x85\xe5\x90\xab\xe6\xb5\xb7\xe9\x87\x8f\xe8\xb5\x84\xe8\xae\xaf\xe7\x9a\x84\xe6\x96\xb0\xe9\x97\xbb\xe6\x9c\x8d\xe5\x8a\xa1\xe5\xb9\xb3\xe5\x8f\xb0\xef\xbc\x8c\xe7\x9c\x9f\xe5\xae\x9e\xe5\x8f\x8d\xe6\x98\xa0\xe6\xaf\x8f\xe6\x97\xb6\xe6\xaf\x8f\xe5\x88\xbb\xe7\x9a\x84\xe6\x96\xb0\xe9\x97\xbb\xe7\x83\xad\xe7\x82\xb9\xe3\x80\x82\xe6\x82\xa8\xe5\x8f\xaf\xe4\xbb\xa5\xe6\x90\x9c\xe7\xb4\xa2\xe6\x96\xb0\xe9\x97\xbb\xe4\xba\x8b\xe4\xbb\xb6\xe3\x80\x81\xe7\x83\xad\xe7\x82\xb9\xe8\xaf\x9d\xe9\xa2\x98\xe3\x80\x81\xe4\xba\xba\xe7\x89\xa9\xe5\x8a\xa8\xe6\x80\x81\xe3\x80\x81\xe4\xba\xa7\xe5\x93\x81\xe8\xb5\x84\xe8\xae\xaf\xe7\xad\x89\xef\xbc\x8c\xe5\xbf\xab\xe9\x80\x9f\xe4\xba\x86\xe8\xa7\xa3\xe5\xae\x83\xe4\xbb\xac\xe7\x9a\x84\xe6\x9c\x80\xe6\x96\xb0\xe8\xbf\x9b\xe5\xb1\x95\xe3\x80\x82" >\n<script type="text/javascript">\n\t\tdocument.write("<script  type=\'text/javascript\' src=\'//news.baidu.com/z/resource/pc_index_banner/pcconf.js?"+new Date().getTime()+"\'><\\/script>");\n\t</script>\n<script type="text/javascript"> window.NEWSLOGURL = \'\r\n'
print(data.decode('utf-8'))