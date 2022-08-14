# -*- coding: utf-8 -*-

"""
---------------------------------------------
    File name:       OrderedList
    Description:     
    Development Env: macOS Monterey 12.4
    Version:         Python 3.8.6
    Author:         xiaoyan
    Date:           8/8/22
---------------------------------------------
"""

from .node import Node

class OrderedList:
    def __init__(self):
        self.head = None

    def add(self, new_node):
        tmp = Node(new_node)
        if self.head is None or \
            self.head.get_data() <= new_node.get_data():
            tmp.set_next(self.head)
        else:
            previous = self.head.get_next()
            self.head.set_next(tmp)
            tmp.set_next(previous)


