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
    """规定左侧为链表头，右侧为链表尾"""
    def __init__(self):
        self.head = None  # 当前节点， 为None表示空链表

    def add_first(self, item):
        """链表头新增"""
        tmp = Node(item)
        tmp.set_next(self.head)
        self.head = tmp

    def add_last(self, item):
        """链表尾新增"""
        curr = self.head

        if curr is None:  #空队列，要修改头结点
            self.add_first(item)
        else:
            curr = self.get_last_node()

            #新增节点
            new_node = Node(item)
            curr.set_next(new_node)


    def get_last_node(self):
        """获取链表最后一个节点，是最早加入的节点"""
        curr, prev = self.get_last_two_nodes()
        return curr

    def get_last_two_nodes(self):
        """获取链表最后两个节点，用于如删除最后一个节点等操作"""
        curr = self.head
        prev = None
        while curr is not None:
            if curr.next is None:  # 找到了最早加入的节点，退出循环
                break
            else:  # 否则继续循环下一个节点
                prev = curr
                curr = curr.next
        return curr, prev




    def is_empty(self):
        return self.head is None

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
        current = self.head
        previous = None  # 头结点没有初始值
        while current is not None:
            if current.get_data() == val:
                break
            else:
                previous = current
                current = current.get_next()

        #解决了只有一个节点和最后一个节点的 删除问题
        current_next = current.get_next() if current is not None else None
        if previous is None:
            # remove第一个元素， 此时没有previous， 故需修改链表的头结点，
            self.head = current_next
        else:
            previous.set_next(current_next)

    def remove_first(self):
        """ 删除第一个节点，只需修改head指针"""
        curr = self.head
        val = ''  #返回被删除的值
        if curr is not None: #只处理非空队列
            val = curr.get_data()
            if curr.next is not None:  #有多个节点时
                self.head = curr.next
            else:  #只有一个节点时, 置为空队列
                self.head = None
        return val


    def remove_last(self ):
        """删除 最早加入的节点(在链表尾)"""
        curr, prev = self.get_last_two_nodes()
        if prev is None:
            # 只有一个元素时，置为空队列
            self.head = None
        else:
            prev.set_next(None)   #删除节点（prev直接接地）

        return curr.data








