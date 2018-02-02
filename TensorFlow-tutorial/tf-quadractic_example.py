# Andrew Ng, deeplearning.ai code

import numpy as np
import tensorflow as tf

# data
coefficients = np.array([[1.], [-20.], [100.]]) # (3,1) matrix
# vars
w = tf.Variable(np.random.randn(),dtype=tf.float32) # parameters
x = tf.placeholder(tf.float32,[3,1])# from dataset
#cost = w**2 - 6*w + 7 # to minimize it, w = 3
#cost = w**2 - 10*w + 25 # to minimize it, w = 5
cost = x[0][0]*w**2 + x[1][0]*w + x[2][0] # to minimize it, w = 5
#train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)
train = tf.train.AdamOptimizer(learning_rate=0.005).minimize(cost)

init = tf.global_variables_initializer()
session = tf.Session()
session.run(init)
print(session.run(w)) # print w

# train
for i in range(5000):
    session.run(train, feed_dict = {x:coefficients})
print(session.run(w))
