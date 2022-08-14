# -*- coding: utf-8 -*-

"""
---------------------------------------------
    File name:       node
    Description:     
    Development Env: macOS Monterey 12.4
    Version:         Python 3.8.6
    Author:         xiaoyan
    Date:           8/9/22
---------------------------------------------
"""



class Node:
    def __init__(self,init_data):
        self.data = init_data
        self.next = None  # 下一个节点的引用


    def get_data(self):
        return self.data


    def get_next(self):
        return self.next


    def set_data(self, new_data):
        self.data = new_data


    def set_next(self,new_next):
        self.next = new_next


    def to_string(self, linked_list=False):
        #输出节点的数据
        #如果是链表，输出当前头结点到链表尾的数据
        #否则就输出当前节点的数据
        if linked_list:
            current = self
            while current is not None:
                if current.get_data() is not None:
                    print(current.get_data(), end='')
                current = current.get_next()

            print('')
        else:
            print(self.data)