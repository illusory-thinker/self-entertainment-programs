# 该程序示例标准计算器(pack+frame方式)

import tkinter as tk # 导入Python标准GUI界面模块
from math import sin,cos,sqrt,tan,exp
root = tk.Tk()  # 创建根窗口
root.title("complex calculator")

displayFrame = tk.Frame(root)
formula = tk.StringVar()
display = tk.Entry(displayFrame, textvariable=formula, font = ('Helvetica', 20), justify = tk.RIGHT, relief = tk.SOLID)
display.pack(side=tk.TOP, expand = tk.YES, fill = tk.BOTH)
displayFrame.pack(side=tk.TOP, expand = tk.YES, fill = tk.BOTH)

boardFrame = tk.Frame(root)
keys = [['C','CE',  'DEL','exp' ],['sin','cos','tan','√'],['(',')','^','/'], ['7','8','9', '*'], ['4', '5', '6', '-'], ['1', '2', '3', '+'], ['+/-', '0', '.','=']]
for line in keys:
    lineFrame = tk.Frame(boardFrame)
    for key in line:
        if '0'<=key<='9' or key == '.':
            tk.Button(lineFrame, text=key, command = lambda f=formula, k=key: f.set(f.get()+k), width=8, font=('Verdana', 12)).pack(side=tk.LEFT)
        elif key=='C' or key =='CE':
            tk.Button(lineFrame, text=key, command = lambda f=formula, k=key: f.set(''), width =8, font=('Verdana', 12)).pack(side=tk.LEFT)
        elif key=='<':
            tk.Button(lineFrame, text=key, command = lambda f=formula, k=key: f.set(f.get()[:-1] if f.get()!="" else ""), width = 8, font=('Verdana', 12)).pack(side=tk.LEFT)
        elif key=='+' or key=='-' or key=='*' or key=='/' :
            tk.Button(lineFrame, text=key, command = lambda f=formula, k=key: f.set(f.get()+k if f.get()!="" else ""), width = 8, font=('Verdana',12)).pack(side=tk.LEFT)
        elif key == '+/-': # 负号
            tk.Button(lineFrame, text=key, command = lambda f=formula, k=key: f.set(f.get()+'-'), width=8, font=('Verdana', 12)).pack(side=tk.LEFT)
        elif key=='DEL' :
            tk.Button(lineFrame, text=key, command = lambda f=formula, k=key: f.set(f.get()[:-1] if f.get()!="" else ""), width = 8, font=('Verdana', 12)).pack(side=tk.LEFT)
        elif key=='(':#左括号
            tk.Button(lineFrame, text=key, command = lambda f=formula, k=key: f.set(f.get()+k), width = 8, font=('Verdana',12)).pack(side=tk.LEFT)
        elif key==')':#右括号
            tk.Button(lineFrame, text=key, command = lambda f=formula, k=key: f.set(f.get()+k if f.get()!="" else ""), width = 8, font=('Verdana', 12)).pack(side=tk.LEFT)
        elif key=='^':#乘方符号
            tk.Button(lineFrame, text=key, command = lambda f=formula, k='**': f.set(f.get()+k if f.get()!="" else ""), width = 8, font=('Verdana', 12)).pack(side=tk.LEFT)
        elif key=='√':#根号
            tk.Button(lineFrame, text=key, command = lambda f=formula, k='sqrt(': f.set(f.get()+k), width = 8, font=('Verdana', 12)).pack(side=tk.LEFT)
        elif key=='sin':#根号
            tk.Button(lineFrame, text=key, command = lambda f=formula, k='sin(': f.set(f.get()+k), width = 8, font=('Verdana', 12)).pack(side=tk.LEFT)
        elif key=='cos':#根号
            tk.Button(lineFrame, text=key, command = lambda f=formula, k='cos(': f.set(f.get()+k), width = 8, font=('Verdana', 12)).pack(side=tk.LEFT)
        elif key=='tan':#根号
            tk.Button(lineFrame, text=key, command = lambda f=formula, k='tan(': f.set(f.get()+k), width = 8, font=('Verdana', 12)).pack(side=tk.LEFT)
        elif key=='exp':#根号
            tk.Button(lineFrame, text=key, command = lambda f=formula, k='exp(': f.set(f.get()+k), width = 8, font=('Verdana', 12)).pack(side=tk.LEFT)
        else: # key == '='
            tk.Button(lineFrame, text=key, command = lambda f=formula, k=key: f.set(eval(f.get())), width = 8, font=('Verdana', 12)).pack(side=tk.LEFT)
    lineFrame.pack(side=tk.TOP)
boardFrame.pack(side=tk.TOP)

tk.mainloop()   # 进入“服务器式”主循环
