# -*- coding: utf-8 -*-

"""
---------------------------------------------
    File name:       deque
    Description:     链表实现双端队列
    Development Env: macOS Monterey 12.4
    Version:         Python 3.8.6
    Author:         xiaoyan
    Date:           8/14/22
---------------------------------------------
"""

from .unorderedlist import UnorderedList


class Deque:
    """
    链表实现双端队列：
    - 规定左侧为双端队列尾端，右侧为头端，
    - 与链表规定的顺序是反的(链表是左头右尾)，所以头、尾的增删操作要注意反一下
    """
    def __init__(self):
        self.unorderedlist = UnorderedList()

    def add_front(self, item):
        """双端队列前端，是链表的尾部"""
        self.unorderedlist.add_last(item)

    def add_rear(self, item):
        """双端队列后端，是链表的头部"""
        self.unorderedlist.add_first(item)



    def remove_front(self):
        """删除双端队列头部元素，即链表的尾部元素"""
        return self.unorderedlist.remove_last()


    def remove_rear(self):
        """删除双端队列尾部，即链表的头部"""
        return self.unorderedlist.remove_first()


    def is_empty(self):
        return self.unorderedlist.is_empty()

    def size(self):
        return self.unorderedlist.length()


    def get_head(self): #开发时查看输出用
        return self.unorderedlist.head

