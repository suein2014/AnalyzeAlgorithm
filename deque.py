# -*- coding: utf-8 -*-

"""
---------------------------------------------
    File name:       deque
    Description:     
    Development Env: macOS Monterey 12.4
    Version:         Python 3.8.6
    Author:         xiaoyan
    Date:           8/8/22
---------------------------------------------
"""

from pythonds import Deque


def main():
    #test_deque()

    t = pal_checker("radar"), pal_checker("kljljlj")
    print(t)




def pal_checker(some_str):
    dq = Deque()

    for char in some_str:
        dq.addRear(char)

    while dq.size() > 1:
        front_char = dq.removeFront()
        rear_char = dq.removeRear()
        if front_char != rear_char:
            return False
    return True





def test_deque():
    d = Deque_My()
    print(d.is_empty())  #True

    d.add_rear(4)
    d.add_rear('dog')
    d.add_front('cat')
    d.add_front(True)

    print(d.size())      # 4
    print(d.is_empty())  # False

    d.add_rear(8.4)
    print(d.remove_rear())  # 8.4

    print(d.remove_front())  # True




class Deque_My:
    def __init__(self):
        self.dq = []

    def add_front(self,item):
        self.dq.append(item)

    def add_rear(self,item):
        self.dq.insert(0, item)

    def remove_front(self):
        return self.dq.pop()

    def remove_rear(self):
        return self.dq.pop(0)

    def is_empty(self):
        return self.dq == []

    def size(self):
        return len(self.dq)




main()