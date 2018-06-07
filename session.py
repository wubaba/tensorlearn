# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 20:59:15 2018
@author: 吴八八
"""
##session
import tensorflow as tf

m1 = tf.constant([[2, 2]])
m2 = tf.constant([[3],
                  [3]])
dot_operation = tf.matmul(m1, m2)


## method1 use session
#sess = tf.Session()
#result1 = sess.run(dot_operation)
#print(result1)
#sess.close()

# method2 use session
with tf.Session() as sess:
    result_ = sess.run(dot_operation)
    print(result_)