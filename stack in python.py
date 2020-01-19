# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 21:12:05 2019

@author: Quantum Mechanics

Perseverance always pays off
"""

class stack:#定义一个栈类
    def __init__(self,lst,maxsize):#栈的形式为列表形式
        self.lst=lst
        self.maxsize=maxsize
    def clear_stack(self):#栈的重置
        self.lst=[]
    def maxsize(self):#栈的尺寸
        return self.maxsize
    def isempty(self):#判断栈是否为空
        if len(self.lst)==0:
            return True
        else:
            return False
    def isfull(self):#判断栈是否为空
        if len(self.lst)==self.maxsize:
            return True
        else:
            return False
    def printstack(self):#打印栈
        for i in self.lst:
            print(i)
    def out(self,m):#出栈函数，尾部出栈,m为出栈操作次数,返回操作后列表，用于调用退栈后列表
        a=len(self.lst)
        if m>a or m<=0:
            print('error')
        else:
            for i in range(0,m):
                self.lst.pop()
        return self.lst
    def outprint(self):#单次退栈，用于调用出栈对象
        return self.lst.pop()
    def insert(self,n):#进栈函数，尾部进栈
        if self.isfull()==True:
            return 'Overflow'
        else:
            self.lst.append(n)
            return self.lst
    def conditions(self,n):#出栈情况只是要进栈个数的函数，也就是卡塔兰数
        a=1
        for i in range(1,n+1):
            a=int((4*i-2)*a/(i+1))
        return a
def postfixexpression(lst):#后缀表达式求值
    lst1=stack([],len(lst))
    for i in lst:#代码精简，同时用上了O(1)的pop()
        if i in range(0,11):
            lst1.insert(i)
        elif i=='+':
            lst1.lst[-1]=lst1.lst[-2]+lst1.lst.pop()
        elif i=='-':
            lst1.lst[-1]=lst1.lst[-2]-lst1.lst.pop()
        elif i=='*':
            lst1.lst[-1]=lst1.lst[-2]*lst1.lst.pop()
        elif i=='/':
            lst1.lst[-1]=lst1.lst[-2]/lst1.lst.pop()
        else:
            print('Invalid character!')
            lst1.clear_stack()
            break
    for i in lst1.lst:#这条代码傻死了，因为是单元素，然而修正前的更傻，因为是print而无法在外部调用
        return i
def nifixtosuffix(lst):
    num=[]
    lst1=stack([],len(lst))
    for i in lst:
        if i in ['+','-','*','/','(',')']:
            if i in ['*','/','(']:#直接进栈
                lst1.insert(i)
            elif i == ')':
                while lst1.lst[-1]!='(':
                    num.append(lst1.lst.pop())#退栈至左括号，此处不用担心空栈报错，因为有右括号必有左括号
                lst1.lst.pop()#'('出栈
            else:#此处注意空栈判断，因为单纯循环的话空栈用lst1.lst[-1]会报错
                while lst1.isempty()==False:#退栈至'('，否则直接退空
                    if lst1.lst[-1]!='(':
                        num.append(lst1.lst.pop())
                    else:#空栈跳出循环
                        break
                lst1.insert(i)
        else:
           num.append(i)
    num=num+lst1.lst[::-1]#栈倒置添加到列表尾部
    return num
#postfixexpression([2,3,4,'+','*',8,2,'/','[','-'])
#print(postfixexpression([2,3,4,'+','*',8,2,'/','-']))
#print(nifixtosuffix([2,'*','(',3,'+',4,')','-',8,'/',2]))
            
     
