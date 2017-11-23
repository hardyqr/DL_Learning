"""
A very simple MNIST classifier.

See extensive documentation at
http://tensorflow.org/tutorials/mnist/beginners/index.md
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

'''Import data'''
from tensorflow.examples.tutorials.mnist import input_data

import tensorflow as tf


#这堆flag什么意思?

flags = tf.app.flags
FLAGS = flags.FLAGS
flags.DEFINE_string('data_dir', '/tmp/data/', 'Directory for storing data')

mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)


'''Create the model'''
x = tf.placeholder(tf.float32, [None, 784])
# None means the dimension can be of any length
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)

'''Define loss and optimizer'''
y_ = tf.placeholder(tf.float32, [None, 10])
# this is for the ground trutj labels
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)


'''Train'''
sess = tf.InteractiveSession()
tf.global_variables_initializer().run()
for _ in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict = {x: batch_xs, y_: batch_ys})
  # We run train_step feeding in the batches data to replace the placeholders.


'''Test trained model'''
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
# tf.argmax returns the index with the largest value across axes of a tensor.
# tf.equal returns the truth value of (x == y) element-wise.
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
# tf.cast casts a tensor to a new type.
print(sess.run(accuracy, feed_dict = {x: mnist.test.images, y_: mnist.test.labels}))
