# -*- coding: utf-8 -*-

"""
---------------------------------------------
    File name:       queue
    Description:     链表实现队列
    Development Env: macOS Monterey 12.4
    Version:         Python 3.8.6
    Author:         xiaoyan
    Date:           8/14/22
---------------------------------------------
"""

from .unorderedlist import UnorderedList

class Queue:
    """
    链表实现队列：
    - 队列规定：左尾右头，
    - 与链表规定的顺序是反的(链表是左头右尾)， ，所以头、尾的增删除操作要注意反一下
    """
    def __init__(self):
        self.unorderedlist = UnorderedList()

    def enqueue(self, item):
        """队列尾端加，链表是在头端加"""
        self.unorderedlist.add_first(item)

    def is_empty(self):
        return self.unorderedlist.is_empty()

    def size(self):
        return self.unorderedlist.length()



    def dequeue(self):
        """队列FIFO，队列头(右侧)弹出。 但链表里右侧是尾部。
        最早加入的元素在链表尾部，所以要删除链表最后的元素。用remove_last"""
        return self.unorderedlist.remove_last()

    def get_head(self): #开发时查看输出用
        return self.unorderedlist.head


