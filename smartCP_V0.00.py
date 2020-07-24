## 双色球预测小程序  版本号：V0.00

## 子程序1：更新开奖数据的算法设计：
##①从文件中读入红球历史开奖数据到数组a；
##
##②输入当期开奖的6个红球存入列表，同时生成当期开奖的数组b；
##
##③数组b与数组a最后一行的所有元素，逐位元素进行比较、运算，生成中间数组C；
##  如果数组b当前位置元素的值为0，元素值保持0不变；将其写入中间数组C的对应位置；
##  如果数组b当前位置元素的值为1,则对数组a最后一行的当前元素值加1，将其写入中间数组C的对应位置；
##
##④将数组c追加到数组a的最后一行，
##
##⑤将更新后的数组a写入新文件

##子程序2：统计程序的算法设计（更新中)

import numpy as np
import os as os

def readhistory():
    print("1.导入历史中奖红球数据到数组a")
    a=np.loadtxt("e:\\caipiao\\redhistory.csv",dtype=np.int,delimiter=",")
##    print(a)
##    print("过程编写中.....")
##    print("返回数组a")
    return a   ##数组a无法返回到主程序，如何处理？

##def readcurrent():
##    print("2.读入当期中奖红球数据到数组b")
##    list_cur=[2020061,8,17,24,26,27,31]
##    b=np.ones((34),dtype=np.int)
##    b[0]=list_cur[0]
##    print("转换前b的值是：",b)
##    for i in range(1,7):
##        temp=list_cur[i]
##        b[temp]=0  
##    print("转换后b的值是：",b)
##    
##def create():
##    print("3.创建临时数组c")
##    print("过程编写中.....")
##    print("返回数组c")
##    
##def updatehistory():
##    print("4.更新当期中奖红球数据到数组a")
##    print("结果写入新文件.....")
##    print("返回新文件")
##    print("读取验证")
    
def main():
    print("准备开始。。。")
    history = readhistory()    #代涛指导，将函数值 返回给变量，即可以将数组的值 带到主程序；
    print(history)
##    readcurrent()
##    create()
##    updatehistory()
##    print("数据更新完毕。。。")
    
main()
##print(a) ##数组a的值无法从子程序返回到主程序，如何处理？
