# ！/usr/bin/env python
# -*-coding:Utf-8 -*-
# Explanation: tkinter_test
# Author: Peng Hu
import tkinter as tk


# 定义计数器应用程序类
class CounterApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("计数器")

        # 初始化计数值
        self.count = 0

        # 创建标签显示计数值
        self.label = tk.Label(self.root, text=str(self.count), font=('Arial', 48))
        self.label.pack()

        # 创建增加按钮
        self.increase_button = tk.Button(self.root, text="增加", command=self.increase)
        self.increase_button.pack(side="left")

        # 创建减少按钮
        self.decrease_button = tk.Button(self.root, text="减少", command=self.decrease)
        self.decrease_button.pack(side="right")

    # 增加计数函数
    def increase(self):
        self.count += 1
        self.label.config(text=str(self.count))

    # 减少计数函数
    def decrease(self):
        self.count -= 1
        self.label.config(text=str(self.count))

    # 运行应用程序
    def run(self):
        self.root.mainloop()


# 创建并运行计数器应用程序
if __name__ == "__main__":
    app = CounterApp()
    app.run()