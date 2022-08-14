# -*- coding: utf-8 -*-

"""
---------------------------------------------
    File name:       task
    Description:     
    Development Env: macOS Monterey 12.4
    Version:         Python 3.8.6
    Author:         xiaoyan
    Date:           8/7/22
---------------------------------------------
"""

import random


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages


    def wait_time(self, current_time):
        return current_time - self.timestamp


