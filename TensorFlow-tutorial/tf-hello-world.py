# Freddy @ BNU 387
# Aug 30 2017

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

'''hello world'''
hello = tf.constant('------Hi--TensorFlow!------')
sess = tf.Session()
print(sess.run(hello))


'''add and multiply'''
a = tf.constant(2)
b = tf.constant(3)

with tf.Session() as sess:
    print("a=2, b=3")
    print("Addition of constants: %i"% sess.run(a+b) )
    print("Multiplication of constants: %i"% sess.run(a*b) )


'''the use of tf.placeholder'''
a = tf.placeholder(tf.int32)
b = tf.placeholder(tf.int32)

# build compute graph
add = tf.add(a, b)
mul = tf.multiply(a, b)
with tf.Session() as sess:
    print("Addition of constants: %i" % sess.run(add, feed_dict={a: 2, b: 3}))
    print("Multiplication of constants: %i" % sess.run(mul, feed_dict={a: 2, b: 3}))

'''matmul: matrix multiplication'''
m1 = tf.placeholder(tf.float32,shape=(1,2)) #1x2
m2 = tf.placeholder(tf.float32,shape=(2,1)) #2x1
product = tf.matmul(m1, m2)
with tf.Session() as sess:
    print("matmul, 1x2 * 2x1 = 1x1" )
    print(sess.run(product, feed_dict= {m1:[[3.,3.]] , m2:[[2.],[2.]] }))


'''linear regression'''

# parameters
learning_rate = 0.1
training_epochs = 2000
display_step = 50

# training data
train_X = np.array([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,7.042,10.791,5.313,7.997,5.654,9.27,3.1])
train_Y = np.array([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,2.827,3.465,1.65,2.904,2.42,2.94,1.3])

# Inputs
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

# model weights
W = tf.Variable()
b = tf.Variable()

