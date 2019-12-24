#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 视频破解.py
# @Author: 未衬


# url解析 vip视频播放地址的模块 做url加密的
from urllib import parse

# TK 如果出现错误会返回一个消息
import tkinter.messagebox as msgbox

# 做桌面编程的
import tkinter as tk

# 控制浏览器的
import webbrowser

# 正则表达式
import re

class APP:
    # 魔术方法
    # 初始化用的
    def __init__(self, width=500, height=300):
        self.w = width
        self.h = height
        self.title = 'vip视频破解助手'
        # 软件名
        self.root = tk.Tk(className=self.title)

        # vip视频播放地址 StringVar() 定义字符串变量
        self.url = tk.StringVar()

        # 定义选择哪个播放源
        self.v = tk.IntVar()

        # 默认为1
        self.v.set(1)

        # Frame空间
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)

        # 控件内容设置
        group = tk.Label(frame_1, text='视频播放通道：', padx=0)
        tb = tk.Radiobutton(frame_1, text='通道1', variable=self.v, value=1, width=10, height=3)
        tb2 = tk.Radiobutton(frame_1, text='通道2', variable=self.v, value=2, width=10, height=3)
        tb3 = tk.Radiobutton(frame_1, text='通道3', variable=self.v, value=3, width=10, height=3)
        tb4 = tk.Radiobutton(frame_1, text='通道4', variable=self.v, value=4, width=10, height=3)
        tb5 = tk.Radiobutton(frame_1, text='通道5', variable=self.v, value=5, width=10, height=3)
        lable = tk.Label(frame_2, text='请输入视频连接：')

        # 输入框声明
        entry = tk.Entry(frame_2, textvariable=self.url, highlightcolor='Fuchsia', highlightthickness=1, width=35)
        play = tk.Button(frame_2, text='播放', font=('楷体', 12), fg='Purple', width=2, height=1, command=self.video_play)

        # 控件布局 显示控件在你的软件上
        frame_1.pack()
        frame_2.pack()

        # 确定控件的位置 wow 行 column 列
        group.grid(row=0, column=0)
        tb.grid(row=0, column=1)
        tb2.grid(row=0, column=2)
        tb3.grid(row=0, column=3)
        tb4.grid(row=0, column=4)
        tb5.grid(row=0, column=5)
        lable.grid(row=1, column=0)
        entry.grid(row=1, column=1)

        # ipadx x方向的外部填充 ipady y方向的内部填充
        play.grid(row=1, column=3, ipadx=10, ipady=10)

    def video_play(self):
            # 视频解析网站地址
            port1 = 'http://www.wmxz.wang/video.php?url='
            port2 = 'http://www.a305.org/weixin.php?url='
            port3 = 'http://www.vipjiexi.com/tong.php?url='
            port4 = 'http://jx.aeidu.cn/index.php?url='
            port5 = 'http://tv.dsqndh.com/?jk=http%3A%2F%2Fjqaaa.com%2Fjx.php%3Furl%3D&url='
            portArr = {"1":port1,"2":port2,"3":port3,"4":port4,"5":port5}
            port = portArr[str(self.v.get())];

            # 正则表达式判定是否为合法连接
            if re.match(r'^https?:/{2}\w.+$', self.url.get()):
                # 拿到用户输入的视频网址
                ip = self.url.get()

                # 视频连接加密
                ip = parse.quote_plus(ip)

                # 用浏览器打开网址
                webbrowser.open(port + ip)

            else:
                msgbox.showerror(title='错误', message='视频链接地址无效，请重新输入！')

    # 启动GUI程序的函数
    def loop(self):
            self.root.resizable(True, True)
            self.root.mainloop()

if __name__ == "__main__":
    app = APP()
    app.loop()