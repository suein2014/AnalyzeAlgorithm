# -*- coding: utf-8 -*-

"""
---------------------------------------------
    File name:       printqueue
    Description:     模拟打印机打印任务的队列，
                        -允许设置打印总时间，1小时
                        -设置打印机每分钟打印多少页： 10页(质量差)， 5页(打印质量好)
    Development Env: macOS Monterey 12.4
    Version:         Python 3.8.6
    Author:         xiaoyan
    Date:           8/7/22
---------------------------------------------
"""

from pythonds.basic import Queue
from . import printer, task

import random


def main():
    for i in range(10):
        simulation(3600,5)



def simulation(num_seconds, pages_per_minute):
    """
    模拟打印机，1小时里的打印过程(实验室里有10个学生，每小时打印20次，平均每3分钟打印一次)
    :param num_seconds: 打印总时间
    :param pages_per_minute:  打印机每分钟打印页数
    :return:
    """
    lab_printer = printer.Printer(pages_per_minute)
    print_q = Queue()
    waiting_times = []

    for current_second in range(num_seconds):
        if new_print_task():
            tsk = task.Task(current_second)
            print_q.enqueue(tsk)

        if (not lab_printer.busy()) and (not print_q.isEmpty()):
            next_tsk = print_q.dequeue()
            waiting_times.append(next_tsk.wait_time(current_second))
            lab_printer.start_next(next_tsk)

        lab_printer.tick()
    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average Wait {:6.2f} secs {:3d} tasks remaining.".format(float(average_wait), print_q.size()))


def new_print_task():
    """
    - 判断是否有新打印任务。
    - 每180秒有一个打印任务（从随机数选取180å）
    """
    num = random.randrange(1, 181)
    return num == 180


main()