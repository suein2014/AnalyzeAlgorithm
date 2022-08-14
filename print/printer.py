# -*- coding: utf-8 -*-

"""
---------------------------------------------
    File name:       printer
    Description:     
    Development Env: macOS Monterey 12.4
    Version:         Python 3.8.6
    Author:         xiaoyan
    Date:           8/7/22
---------------------------------------------
"""


class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm  #  每页纸的打印速度，质量差的每分钟10页，好的5页
        self.current_task = None  # 当前的打印任务，是一个task类的对象
        self.time_remaining = 0


    def tick(self):
        if self.current_task != None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        return self.current_task != None

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate


