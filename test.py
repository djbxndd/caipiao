## 1.文件逐行读取知识点：https://www.cnblogs.com/Kingfan1993/p/9570079.html


#-*- coding: UTF-8 -*-
import numpy as np
import os as os

os.chdir("e:\\caipiao\\")
filename="current_data - 副本.csv"

#获取文件的行数；
count=0
f = open(filename,"r")
for line in f.readlines():
    count=count+1
print("files has lines are:",count)


for line in open(filename):    
    a=(line.split())

##    for i in a:
##        b=(i.split(","))
##        c=np.array(b)
##        print(c)
##print(c.ndim)
##print(c)



