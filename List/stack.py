# -*- coding: utf-8 -*-

"""
---------------------------------------------
    File name:       stack
    Description:     
    Development Env: macOS Monterey 12.4
    Version:         Python 3.8.6
    Author:         xiaoyan
    Date:           8/14/22
---------------------------------------------
"""


from .unorderedlist import UnorderedList
from .node import Node


class Stack:
    """链表实现栈，
    - 链表左头右尾， 栈左底右顶(顶端即右端操作增删)。
    """
    def __init__(self):
        self.unorderedlist = UnorderedList()

    def push(self, new_node):
        self.unorderedlist.add_last(new_node)

    def peek(self):
        return self.unorderedlist.get_last_node()

    def is_empty(self):
        return self.unorderedlist.is_empty()

    def size(self):
        return self.unorderedlist.length()

    def pop(self):
        return self.unorderedlist.remove_last()

    def get_head(self): #开发时查看输出用
        return self.unorderedlist.head