# -*- coding:utf8 -*-
#引入需要用到的opencv和numpy库
import cv2
import numpy as np

# 定义实现图像卷积运算的函数
def convolve(img,kernel):
    # 获取图片和卷积核的宽高
    wImg = img.shape[0] #图片的宽度wImg
    hImg = img.shape[1] # 图片的高度hImg
    h, w = kernel.shape # 卷积核的高度h和宽度w
    # 初始化一张同样大小的图片作输出的图片
    output = np.zeros_like(a=img)
#正片开始喽
#第一步，旋转卷积核
    array1= kernel.reshape(kernel.size)#变成kernel元素个数维的数组，每个维度只有一个元素
    array1= array1[::-1]#数组倒置
    kernel= array1.reshape(kernel.shape)#重构
#第二步,将矩阵上下各添加一个全零行，左右各添加一个全零列
    img=np.insert(img,0,[0]*hImg,0)#添加全零行至第一行
    img=np.append(img,[[0]*hImg],axis=0)#添加全零行至最后一行
    img=np.insert(img,0,values=0,axis=1)#添加全零列至第一列
    img=np.insert(img,hImg+1,values=0,axis=1)#添加全零列至最后一列
#第三步，对原矩阵每一个元素进行Hadamard乘积
    for i in range(1,wImg+1):
        for j in range(1,hImg+1):
            tinymatrics=img[i-1:i+2,j-1:j+2]#取小矩阵
            ker=tinymatrics*kernel#Hadamard乘积
            sum1=ker.sum()#计算各元素和
            if sum1>=255:#边界处理
                sum1=255
            elif sum1<=0:
                sum1=0
            output[i-1][j-1]=sum1#将结果添加到输出图片中
    return output
#正片结束，撒花❀❀❀
img = cv2.imread("balloon.jpg",cv2.IMREAD_GRAYSCALE)#导入图片
kernel = np.array([[ -1, 0,-1],#设置卷积核(这是大名鼎鼎的边缘检测卷积核！)
                   [  0, 4, 0],
                   [ -1, 0,-1]])
result = convolve(img,kernel)#卷积目标图片
cv2.imwrite("convolved.jpg", result)#输出并保存结果
