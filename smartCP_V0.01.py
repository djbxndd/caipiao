## 双色球预测小程序  版本号V0.01

## 子程序1：更新开奖数据的算法设计：
##①从文件中读入红球历史开奖数据到二维数组a；
##
##②输入当期开奖的6个红球存入列表，同时生成当期开奖的一维数组b；
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


print("1.导入历史中奖红球数据到【二维数组a（1行34列）】")
a=np.loadtxt("e:\\caipiao\\redhistory.csv",dtype=np.int,delimiter=",")
np.resize(a,(1,34))
print(a.ndim,a.shape,a.size)
print("历史中奖数据是：\n",a)

print("2.读入当期中奖红球数据到数组b【（一维数组，34列）】")
list_cur=[2020061,8,17,24,26,27,31]
b=np.ones((34),dtype=np.int)
print(b)

b[0]=list_cur[0]
print("转换前b的值是：\n",b)
for i in range(1,7):  ##从第二个元素开始转换，因为第一个元素是期号；
    temp=list_cur[i]
    b[temp]=0  
print("转换后b的值是：\n",b)

c=b  ##直接赋值的方法拷贝；
print("3.创建临时数组c，其")
print("复制后的数组C的值是：\n",c)
for i in range(1,34):
    if(b[i]==1):
        c[i]=a[i]+b[i]
     
print("更新后的数组C的值是：\n",c)

print("4.更新当期中奖红球数据到数组a")

d=np.vstack([a,c])   ##在二维数组a的尾部追加一行（一维数组）
print("更新后的数组a的值是：\n",d)
print("更新后的数组a的维度值、秩分别是：\n",d.shape,d.ndim)
