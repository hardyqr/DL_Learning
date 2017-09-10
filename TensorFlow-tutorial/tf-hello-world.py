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
'''
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
n_samples = train_X.shape[0]

# model weights
W = tf.Variable(np.random.randn(), name = "weight")
b = tf.Variable(np.random.randn(), name = "bias")


activation = tf.add(tf.multiply(W,X),b)


cost = tf.reduce_sum(tf.pow(activation - Y,2)/(2*int(n_samples)))
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)


init = tf.initialize_all_variables()


with tf.Session() as sess:
    sess.run(init)

    for epoch in range(training_epochs):
        for (x,y) in zip(train_X,train_Y):
            sess.run(optimizer, feed_dict = {X:x, Y:y})

            # display logs per epoch step
            if(epoch % display_step == 0):
                print("Epoch: %i" % (epoch + 1), "cost=",\
                        "{:.9f}".format(sess.run(cost, feed_dict={X:train_X, Y:train_Y})))#???
                print("W=", sess.run(W),"b=",sess.run(b))

    print("done!")
    print("Epoch: %i" % (epoch + 1), "cost=",\
            "{:.9f}".format(sess.run(cost, feed_dict={X:train_X, Y:train_Y})))#???
    print("W=", sess.run(W),"b=",sess.run(b))

    # graphical display
    plt.plot(train_X, train_Y, 'ro', label = "original data")
    plt.plot(train_X, sess.run(W)*train_X + sess.run(b), label = "fitted line")
    plt.legend()
    plt.show()

'''
'''logistic regression'''
# MNIST
'''
# import MNIST data
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

# parameters
learning_rate = 0.01
training_epochs = 100
batch_size = 50
display_step = 1

# tf Graph Input
x = tf.placeholder(tf.float32, [None, 784]) # mnist data image of shape 28*28=784
y = tf.placeholder(tf.float32, [None, 10]) # 0-9 digits recognition => 10 classes

# Set model weights
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# Construct model
pred = tf.nn.softmax(tf.matmul(x, W) + b) # Softmax

# Minimize error using cross entropy
#cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(pred), reduction_indices=1))
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels = y,logits = pred))

# Gradient Descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cross_entropy)

# Initializing the variables
init = tf.global_variables_initializer()

# Launch the graph
with tf.Session() as sess:
    sess.run(init)

    # Training cycle
    for epoch in range(training_epochs):
        avg_cost = 0.
        total_batch = int(mnist.train.num_examples/batch_size)
        # Loop over all batches
        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            # Run optimization op (backprop) and cost op (to get loss value)
            _, c = sess.run([optimizer, cross_entropy], feed_dict={x: batch_xs,
                                                          y: batch_ys})
            # Compute average loss
            avg_cost += c / total_batch
        # Display logs per epoch step
        if (epoch+1) % display_step == 0:
            print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(avg_cost))

    print("Optimization Finished!")

    # Test model
    correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    # Calculate accuracy
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print("Accuracy:", accuracy.eval({x: mnist.test.images, y: mnist.test.labels}))
'''

'''MNIST for expert'''

# import MNIST data
from tensorflow.examples.tutorials.mnist import input_data
#mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)
mnist = input_data.read_data_sets("/Users/Fangyu/Documents/GitHub/DL_Learning/test_with_MINST/MNIST_data/", one_hot = True)
#mnist = input_data.read_data_sets('data/fashion', one_hot = True)

def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev = 0.1)
    # [filter_height, filter_width, in_channels, out_channels]
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape = shape)
    return tf.Variable(initial)

def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides = [1,1,1,1], padding = 'SAME')

def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize = [1,2,2,1], strides = [1,2,2,1], padding = 'SAME')

# parameters
learning_rate = 1e-3
iterations = 2000
batch_size = 100


# tf Graph Input
x = tf.placeholder(tf.float32, [None, 784]) # mnist data image of shape 28*28=784
y = tf.placeholder(tf.float32, [None, 10]) # 0-9 digits recognition => 10 classes

x_image = tf.reshape(x,[-1, 28,28,1])


# first convolutional layer
W_conv1 = weight_variable([6, 6, 1 ,32])
b_conv1 = bias_variable([32])

h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1)+b_conv1)# 28 x 28
h_pool1 = max_pool_2x2(h_conv1)# 14 x 14

# second convolutional layer 
W_conv2 = weight_variable([6,6,32,64])
b_conv2 = bias_variable([64])

h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2)+b_conv2) # 14 x 14
h_pool2 = max_pool_2x2(h_conv2) # 7 x 7

# third convolutional layer 
W_conv3 = weight_variable([4,4,64,64])
b_conv3 = bias_variable([64])

h_conv3 = tf.nn.relu(conv2d(h_pool2, W_conv3)+b_conv3) # 7 x 7
h_pool3 = max_pool_2x2(h_conv3) # 4 x 4


# fourth convolutional layer
W_conv4 = weight_variable([4,4,64,128])
b_conv4 = bias_variable([128])

h_conv4 = tf.nn.relu(conv2d(h_pool3, W_conv4)+b_conv4) # 4 x 4
#h_pool3 = max_pool_2x2(h_conv3) # 4 x 4

# densely connected layer
W_fc1 = weight_variable([4*4*128, 1024])
b_fc1 = bias_variable([1024])

h_conv4_flat = tf.reshape(h_conv4, [-1, 4*4*128])
h_fc1 = tf.nn.relu(tf.matmul(h_conv4_flat, W_fc1) + b_fc1)

# dropout layer
keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# readout layer
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])

y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2

cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels = y,logits = y_conv))
train_step = tf.train.AdamOptimizer(learning_rate).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(iterations):
        batch = mnist.train.next_batch(batch_size)
        if i%100 == 0 :
            train_accuracy = accuracy.eval(feed_dict={x:batch[0], y:batch[1], keep_prob: 1.0})
            print('step %d, training accuracy %.4f' % (i, train_accuracy))
        else:
            train_step.run(feed_dict = {x:batch[0], y:batch[1], keep_prob: 0.5})

    print('test accuracy %.4f' % accuracy.eval(feed_dict={
      x: mnist.test.images, y: mnist.test.labels, keep_prob: 1.0}))
