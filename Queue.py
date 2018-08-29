创建一个队列(先进先出)
FIFO
q = Queue（）
q.put('hello')进
q.put('abc')出
q.get()
qsize()返回队列数据的长度
empty()检查队列是否为空，为空返回true
full()检查队列是否满了，满为true

put(obj[,block[,timeout]])
将一个对象放入队列中
当队列已满是时，再调用put向队列添加元素
此时元素添加不到队列中，put（）会一直等待，直到队列中有空位为止
block 是否阻塞程序执行，默认值是True，如果是False，则不会等待空位，如果有位置则添加，没位置则报错
      因此使用时一定要处理异常
timeout 最大的等待时间，默认值-1，超过最大时间，则报错，queue.Full
close()关闭，不能向队列中添加数据

------------------------------------------------
练习 建立两个进程添加/读取队列的数据
from multiprocessing import Process,Queue
import time
#向队列中添加数据
def make_data(q):
    while True:
        q.put('进程1添加的数据')
        print('数据已添加')
        time.sleep(1)
    pass
#从队列中提取数据
def read_data(q):
    while True:
        data = q.get()
        print(data)
        time.sleep(1)
    pass
if __name__ == '__main__':
    q = Queue()
    n1 = Process(target=make_data,args=(q,))
    n2 = Process(target=read_data,args=(q,))

    n1.start()
    n2.start()

    n1.join()
    n2.join()
