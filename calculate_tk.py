# -*- coding: utf-8 -*-

"""
---------------------------------------------
    File name:       calculate
    Description:     参考：https://blog.51cto.com/u_1760061/3102559
    Development Env: macOS Monterey 12.4
    Version:         Python 3.8.6
    Author:         xiaoyan
    Date:           8/12/22
---------------------------------------------
"""

import tkinter

#mac下的button背景色支持不好，
#pip3 install tkmacosx 模块
#

from tkmacosx import Button

#窗口
window = tkinter.Tk()

window.title('计算器')
#window.geometry('250x190') #网上的代码的宽度设置
window.geometry('510x500')

font_style = tkinter.font.Font(family="Lucida Grande", size=15)


def add(n):
    n1 = inp.get()  #n1号文本框的值
    inp.delete(0, len(n1))  #清空文本框
    inp.insert(0,  n1 + str(n))  #插入其为新的值



def calc():
    n1 = inp.get()
    inp.delete(0, len(n1))
    inp.insert(0, str(eval(n1)))


def clear():
    n1 = inp.get()
    inp.delete(0, len(n1))


#删最后一个字符
def back():
    n1 = inp.get()
    inp.delete(len(n1)-1, len(n1))


def ab():
    n1 = inp.get()
    inp.delete(0, len(n1))
    inp.insert(0, str(eval(n1) * (-1)))



#文本框
inp = tkinter.Entry(window, width=55)
inp.grid(row=0, column=0, ipady=20, columnspan=5)


#for循环创建数字0-9按钮
for i in range(0, 3):
    for j in range(1, 4):
        n = j + i * 3
        btn = tkinter.Button(window, text=str(j+i*3),
                             width=10,height=5 , font=font_style, command=lambda n=n: add(n))
        btn.grid(row=i+2,column=j-1)

btn_width = 120

Button(window, width=btn_width, height=btn_width/2, text='C',command=clear).grid(row=1, column=0)
Button(window, width=btn_width, height=btn_width/2, text='←',command=back).grid(row=1, column=1)
Button(window, width=btn_width, height=btn_width/2, text='+/-',command=ab).grid(row=1, column=2)


Button(window, width=btn_width, height=btn_width/2, text="+", bg="#f70", fg="white",
       command=lambda: add("+")).grid(row=1, column=4)
Button(window, width=btn_width, height=btn_width/2, text="-", bg="#f70", fg="#fff", command=lambda:add("-")).grid(row=2, column=4)
Button(window, width=btn_width, height=btn_width/2, text="×", bg="#f70", fg="#fff", command=lambda:add("*")).grid(row=3, column=4)
Button(window, width=btn_width, height=btn_width/2, text="÷", bg="#f70", fg="#fff", command=lambda:add("/")).grid(row=4, column=4)
Button(window, width=btn_width, height=btn_width/2, text="0", command=lambda:add("0")).grid(row=5, column=0, columnspan=2)
Button(window, width=btn_width, height=btn_width/2, text="=", bg="#f70", fg="#fff", command=calc).grid(row=5, column=4)
Button(window, width=btn_width, height=btn_width/2, text=".", command=lambda: add(".")).grid(row=5, column=2)






'''
网上的代码宽度设置

#文本框
inp = tkinter.Entry(window, width=25)
inp.grid(row=0, column=0, columnspan=5)

#for循环创建数字0-9按钮
for i in range(0, 3):
    for j in range(1, 4):
        n = j + i * 3
        btn = tkinter.Button(window, text=str(j+i*3),
                             width=5, command=lambda n=n: add(n))
        btn.grid(row=i+2,column=j-1)

Button(window,width=50,text='C',command=clear).grid(row=1, column=0)
Button(window,width=50,text='←',command=back).grid(row=1, column=1)
Button(window,width=50,text='+/-',command=ab).grid(row=1, column=2)


Button(window, width=50, text="+", bg="#f70", fg="white",
       command=lambda:add("+")).grid(row=1, column=4)
Button(window,width=50, text="-", bg="#f70", fg="#fff", command=lambda:add("-")).grid(row=2, column=4)
Button(window,width=50, text="×", bg="#f70", fg="#fff", command=lambda:add("*")).grid(row=3, column=4)
Button(window,width=50, text="÷", bg="#f70", fg="#fff", command=lambda:add("/")).grid(row=4, column=4)
Button(window,width=12,text="0", command=lambda:add("0")).grid(row=5, column=0, columnspan=2)
Button(window,width=50,text="=", bg="#f70", fg="#fff", command=calc).grid(row=5, column=4)
Button(window,width=50, text=".", command=lambda:add(".")).grid(row=5, column=2)

'''






window.mainloop()