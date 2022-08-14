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
    def __init__(self):
        self.unorderedlist = UnorderedList()

    def push(self, new_node):
        self.unorderedlist.add_item(new_node)

    def peek(self):
        return self.unorderedlist.head

    def is_empty(self):
        self.unorderedlist.is_empty()

    def size(self):
        return self.unorderedlist.length()

    def pop(self):

        del_val = self.unorderedlist.head.get_data()
        print('dd',del_val)
        second_node = self.unorderedlist.head.next
        print('second', second_node.get_data())
        self.unorderedlist.head = second_node
        self.unorderedlist.remove(del_val)
        return del_val




s = Stack()

lst = [1, 'dog2', '----3']
for i in lst:
    s.push(i)


#print(s.size())
data = s.peek()
data.to_string()
data.to_string(True)



s.pop()

data = s.peek()
data.to_string()
data.to_string(True)


