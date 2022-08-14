# -*- coding: utf-8 -*-

"""
---------------------------------------------
    File name:       linklist
    Description:     
    Development Env: macOS Monterey 12.4
    Version:         Python 3.8.6
    Author:         xiaoyan
    Date:           8/8/22
---------------------------------------------
"""
from .node import Node


class UnorderedList:
    def __init__(self):
        self.head = None  # 当前节点， 为None表示空链表

    def add_item(self, item):
        tmp = Node(item)
        tmp.set_next(self.head)
        self.head = tmp

    def is_empty(self):
        return self.head == None

    def length(self):
        """获取链表长度， 需要遍历链表"""
        current = self.head
        cnt = 0
        while current is not None:
            cnt += 1
            current = current.get_next()
        return cnt

    def search(self, val):
        current = self.head
        while current is not None:
            if current.get_data() == val:
                return True
            current = current.get_next()
        return False

    def remove(self, val):

        if self.head.next is None:
            #就一个节点
            self.head = None
            return

        current = self.head
        previous = None  # 头结点没有初始值
        while current is not None:
            if current.get_data() == val:
                break
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            # remove第一个元素， 此时没有previous， 故需修改链表的头结点，
            # 问题： 不需要判断current有没有下一个节点吗？ 要是一共就1个元素呢？
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())







