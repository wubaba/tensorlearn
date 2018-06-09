# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 22:29:23 2018

@author: 吴八八
"""

###stack(), hstack(), vstack()+
#stack(arrays, axis=0)，arrays可以传数组和列表
#import numpy as np
#a = [[1,2,3],
#     [4,5,6]]
#print("列表a如下：")
#print (a)
#
#print ("增加一维，新维度的下标为0")
#c = np.stack(a, axis = 0)
#print (c)
#
#print ("增加一维，新维度的下标为1")
#c = np.stack(a, axis = 1)
#print (c)
#
###stack 在数组外面套箱子
##


#hstack()水平(按列顺序)把数组给堆叠起来
#vstack()垂直（按照行顺序）的把数组给堆叠起来

import numpy as np
x = [1, 2, 3]
y = [4, 5, 6]
print(np.hstack((x, y)))
print(np.vstack((x, y)))

a=[[1], [2], [3]]
b=[[1], [2], [3]]
c=[[1], [2], [3]]
d=[[1], [2], [3]]
print(np.hstack((a, b, c, d)))
print(np.vstack((a, b, c, d)))







