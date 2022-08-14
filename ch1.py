# -*- coding: utf-8 -*-

"""
---------------------------------------------
    File name:       ch1
    Description:     
    Development Env: macOS Monterey 12.4
    Version:         Python 3.8.6
    Author:         xiaoyan
    Date:           7/31/22
---------------------------------------------
"""

import time
import timeit
from timeit import Timer
import sys

x = list(range(2000000)) # for code_2_10

def main():
    code_2_10()
    #problem_2()
    # problem_1()


def code_2_10():
    '''pop性能观察'''
    popzero = Timer('x.pop(0)', f'from {__name__} import x')
    popend =  Timer('x.pop()', f'from {__name__} import x')


    print('pop zero: ', popzero.timeit(number=1000), ' ms')  # 1.63 ms

    print('pop end: ', popend.timeit(number=1000), ' ms')  # 0.0001 ms








# =============================第2个例子，生成列表4种方法 速度测试

def problem_2():
    t1 = Timer(test1) #注意参数名的写法，是方法名，且没引号、没括号
    print('concat', t1.timeit(number=1000), 'milliseconds')

    t2 = Timer(test2)
    print('append', t2.timeit(number=1000), 'milliseconds')

    t3 = Timer(test3)
    print('comprehension', t3.timeit(number=1000), 'milliseconds')

    t4 = Timer(test4)
    print('list range', t4.timeit(number=1000), 'milliseconds')
    '''
    Output:
    concat 0.110351638 milliseconds
    append 0.08591936 milliseconds
    comprehension 0.043134588 milliseconds
    list range 0.028741200999999994 milliseconds
    '''



def test1():
    lst = []
    for i in range(1000):
        lst += [i]


def test2():
    lst = []
    for i in range(1000):
        lst.append(i)


def test3():
    lst = [i for i in range(1000)]


def test4():
    lst = list(range(1000))  #列表解析式，非常快


# =============================第一个例子，异序词

def problem_1():
    s1 = 'Python'
    s2 = 'typhon'
    s1, s2 = s1.lower(), s2.lower()

    start = time.time()
    ret = anagram_1(s1, s2)
    end = time.time()
    print('ret=', ret)
    print(f'Running time: {float((end - start) * 1000):.4f} ms')

    start = time.time()
    ret = anagram_2(s1, s2)
    end = time.time()
    print('ret=', ret)
    print(f'Running time: {float((end - start) * 1000):.4f} ms')

    start = time.time()
    ret = anagram_3(s1, s2)
    end = time.time()
    print('ret=', ret)
    print(f'Running time: {float((end - start) * 1000):.4f} ms')

    print('---------MAIN END---------')


def anagram_1(s1, s2):
    """O(n*n)"""
    for i in s1:
        if i not in s2:
            print('i=', i, ' not in ', s2)
            return False
    return True


def anagram_2(s1, s2):
    """O(n*n)"""
    alias_s1 = list(s1)
    alias_s2 = list(s2)
    alias_s1.sort()
    alias_s2.sort()
    return alias_s1 == alias_s2


def anagram_3(s1, s2):
    """O(n)"""
    char_pos_s1 = [0] * 26
    char_pos_s2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        char_pos_s1[pos] += 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        char_pos_s2[pos] += 1

    j = 0
    while j < 26:
        if char_pos_s1[j] != char_pos_s2[j]:
            return False
        j += 1
    return True


#if __name__ == '__main__':
main()
