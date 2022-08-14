# -*- coding: utf-8 -*-

"""
---------------------------------------------
    File name:       Queue
    Description:     
    Development Env: macOS Monterey 12.4
    Version:         Python 3.8.6
    Author:         xiaoyan
    Date:           8/6/22
---------------------------------------------
"""

from pythonds import Queue


def main():
    #test_queue()

    ret = joseph_ring(10, 3), joseph_ring(10, 3, 3), joseph_ring(10, 4),\
           joseph_ring(6, 7),
    #输出： (4, 6, 5)

    #ret = hot_potato(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'], 7)

    print(ret)



class Queue_My:
    """队列头在列表右边"""
    def __init__(self):
        self.q = []

    def enqueue(self, item):
        self.q.insert(0, item)  # 时间复杂度 O(n)

    def dequeue(self):
        return self.q.pop()  # O(1)

    def is_empty(self):
        # return len(self.q) == 0
        return self.q == []

    def size(self):
        return len(self.q)

    def peek(self):
        return self.q.index(0)



def hot_potato(nlist, m):
    q = Queue()
    for i in nlist:
        q.enqueue(i)

    while q.size() > 1:
        for i in range(m): #数到m+1的出局? 书上的例子
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()



def joseph_ring(n, m, k=1):
    """循环数n个数(1-n)，从第k个开始数，数到m的出局"""

    #---------产生一个数的队列-----------
    q = Queue()
    for i in range(1, n+1):  # 顺时针 （数  1到n）
    # for i in range(n, 0, -1):  # 逆时针（数 n到1）
        q.enqueue(i)

    for i in range(k-1):  # 从第k个开始数，把前k-1个挪到队列尾部，再接着后面的循环
        q.enqueue(q.dequeue())

    #---------开始循环数数，并移除第m个---------
    while q.size() > 1:
        for i in range(m-1):  # 前m-1个循环入队列
            q.enqueue(q.dequeue())
        q.dequeue()  # 第m个出局

    return q.dequeue()  # 返回最后一个













def test_queue():
    q = Queue_My()
    print(q.is_empty())  # True

    q.enqueue('dog')
    q.enqueue(4)
    q = Queue_My()
    print(q.is_empty())  # True

    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)

    print(q.size())  # 3
    print(q.is_empty())  # False

    q.enqueue(8.4)
    print(q.dequeue())  # 4

    print(q.dequeue())  # 'dog'

    print(q.size())  # 2


main()
