# -*- coding: utf-8 -*-

"""
---------------------------------------------
    File name:       test
    Description:     
    Development Env: macOS Monterey 12.4
    Version:         Python 3.8.6
    Author:         xiaoyan
    Date:           8/14/22
---------------------------------------------
"""



from List.stack import Stack
from List.queue import Queue
from List.deque import Deque



def test():

    # test_deque()
    # test_queue()
    test_stack()






def test_deque():
    dq = Deque()

    dq.add_rear(4)
    dq.add_rear('dog')
    dq.add_front('cat')
    dq.add_front(True)
    print(dq.size())     # 4
    dq.add_rear(8.4)
    print(dq.size())  # 5
    dq.get_head().to_string(True)   #8.4,dog,4,cat,True,
    print(dq.remove_rear())     # 8.4
    dq.get_head().to_string(True)  #  dog,4,cat,True,
    print(dq.remove_front())  # True
    print(dq.size())   # 3
    dq.get_head().to_string(True)  # dog,4,cat,










def test_queue():
    q = Queue()

    lst = [1, 'dog2', '----3']  #输入
    for i in lst:
        q.enqueue(i)    #如果是list，输出为['----3','dog2', 1], 队头在右侧 ,1最先加入， FIFO

    q.get_head().to_string()  # ----3
    print(q.size())  # 3
    print(q.dequeue())  # 1 , FIFO 要弹出最早入队列的元素
    q.get_head().to_string(True)  # ----3dog2




def test_stack():
    s = Stack()


    #lst = [4, 'dog', True, 8.4]  # 输入顺序

    s.push(4)
    s.push('dog')
    s.peek().to_string()  #  dog,
    s.get_head().to_string(True)  # 4,dog,
    s.push(True)
    print(s.size())  # 3
    s.push(8.4)
    print(s.size())  # 4
    s.get_head().to_string(True)  #  4,dog,True,8.4,
    print(s.pop())   #8.4
    s.get_head().to_string(True)  #  4,dog,True,
    print(s.pop())  # True
    s.get_head().to_string(True)   # 4,dog,
    print(s.size())  # 2






test()