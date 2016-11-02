import tensorflow as tf
#from tensorflow.python.ops.constant_op import constant
import numpy as np

# Parameters
learning_rate = 0.001
training_iters = 10000000
batch_size = 128
display_step = 10

# Network Parameters
#n_input = 28 # MNIST data input (img shape: 28*28)
n_input_1=6#Pointcloud data input(X,Y,Z,R,G,B)
n_input_2=12
#n_steps = 28 # timesteps
n_steps=1
n_hidden = 128 # hidden layer num of features
#n_classes = 10 # MNIST total classes (0-9 digits)
n_classes=12#pointcloud total classes(5 furnitures,7 structral parts)


# tf Graph input
#x = tf.placeholder("float", [batch_size, n_steps, n_input_1])
x = tf.placeholder("float", [batch_size, n_steps, n_input_1])

# Tensorflow LSTM cell requires 2x n_hidden length (state & cell)
istate_fw_1 = tf.placeholder("float", [batch_size, 2*n_hidden])
istate_bw_1 = tf.placeholder("float", [batch_size, 2*n_hidden])

istate_fw_2 = tf.placeholder("float", [batch_size, 2*n_hidden])
istate_bw_2 = tf.placeholder("float", [batch_size, 2*n_hidden])

y = tf.placeholder("float", [batch_size, n_classes])

# Define weights
weights_1 = {
    # Hidden layer weights => 2*n_hidden because of foward + backward cells
    'hidden': tf.Variable(tf.random_normal([n_input_1, 2*n_hidden])),
    'out': tf.Variable(tf.random_normal([2*n_hidden, n_input_2]))
}
weights_2 = {
    # Hidden layer weights => 2*n_hidden because of foward + backward cells
    'hidden': tf.Variable(tf.random_normal([n_input_2, 2*n_hidden])),
    'out': tf.Variable(tf.random_normal([2*n_hidden, n_classes]))
}

biases_1 = {
    'hidden': tf.Variable(tf.random_normal([2*n_hidden])),
    'out': tf.Variable(tf.random_normal([n_input_2]))
}

biases_2= {
    'hidden': tf.Variable(tf.random_normal([2*n_hidden])),
    'out': tf.Variable(tf.random_normal([n_classes]))
}


def BiRNN(_X, _istate_fw, _istate_bw, _weights, _biases, _batch_size, _seq_len,_n_input):

    # BiRNN requires to supply sequence_length as [batch_size, int64]
    # Note: Tensorflow 0.6.0 requires BiRNN sequence_length parameter to be set
    # For a better implementation with latest version of tensorflow, check below

    _seq_len = tf.fill([_batch_size], tf.constant(_seq_len, dtype=tf.int64))

    # input shape: (batch_size, n_steps, n_input)
    _X = tf.transpose(_X, [1, 0, 2]) # permute(变换) n_steps and batch_size'''transpose函数，移动位置，把第一个移到第二个，第二个移到第一个'''
    # Reshape to prepare input to hidden activation
    _X = tf.reshape(_X, [-1, _n_input]) # (n_steps*batch_size, n_input)
    # Linear activation
    _X = tf.matmul(_X, _weights['hidden']) + _biases['hidden']

    # Define lstm cells with tensorflow
    # Forward direction cell
    lstm_fw_cell = tf.nn.rnn_cell.BasicLSTMCell(n_hidden, forget_bias=1.0)
    # Backward direction cell
    lstm_bw_cell = tf.nn.rnn_cell.BasicLSTMCell(n_hidden, forget_bias=1.0)

    # Split data because rnn cell needs a list of inputs for the RNN inner loop
    _X = tf.split(0, n_steps, _X) # n_steps * (batch_size, n_hidden)

    # Get lstm cell output
    outputs = tf.nn.bidirectional_rnn(lstm_fw_cell, lstm_bw_cell, _X,
                                            initial_state_fw=_istate_fw,
                                            initial_state_bw=_istate_bw,
                                            sequence_length= _seq_len,)

    # Linear activation
    # Get inner loop last output
    return tf.matmul(outputs[-1], _weights['out']) + _biases['out']


#pred = BiRNN(BiRNN(x, istate_fw_1, istate_bw_1, weights_1, biases_1, batch_size, n_steps,n_input_1),istate_fw_2, istate_bw_2, weights_2, biases_2, batch_size, n_steps,n_input_2)

pred=BiRNN(x, istate_fw_1, istate_bw_1, weights_1, biases_1, batch_size,n_steps ,n_input_1)

with tf.variable_scope('enc'):
    layer_1_output=tf.reshape(BiRNN(x, istate_fw_1, istate_bw_1, weights_1, biases_1, batch_size,n_steps ,n_input_1)
, [128,1,12] )

#with tf.variable_scope('dec'):
#    pred = BiRNN(layer_1_output,istate_fw_2,istate_bw_2,weights_2,biases_2,batch_size,n_steps,n_input_2)


# Define loss and optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(pred, y)) # Softmax loss
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost) # Adam Optimizer

# Evaluate model
correct_pred = tf.equal(tf.argmax(pred,1), tf.argmax(y,1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

# Initializing the variables
init = tf.initialize_all_variables()

# Launch the graph
#六维特征及标签载入
f = open('/Users/Fangyu/Documents/GitHub/Large_Scale_3D_Scene_Recognition_CVPR2017/Point_Cloud_Classification/codes_learning_notes/LSTM_model_pointcloud/beam_1.txt', 'r')
train_data=[]
train_labels=[]
for line in f:
    line=line.split(' ')
    row=[]
    for item in line:
        if '\n' in item:
            p=item.find('\n')
            item=item[0:p]
        row.append(float(item))
    train_data.append(row)
    train_labels.append([1,0,0,0,0,0,0,0,0,0,0,0])
f.close()




f = open('/Users/Fangyu/Documents/GitHub/Large_Scale_3D_Scene_Recognition_CVPR2017/Point_Cloud_Classification/codes_learning_notes/LSTM_model_pointcloud/board_1.txt', 'r')
for line in f:
    line=line.split(' ')
    row=[]
    for item in line:
        if '\n' in item:
            p=item.find('\n')
            item=item[0:p]
        row.append(float(item))
    train_data.append(row)
    train_labels.append([0,1,0,0,0,0,0,0,0,0,0,0])
f.close()

f = open('/Users/Fangyu/Documents/GitHub/Large_Scale_3D_Scene_Recognition_CVPR2017/Point_Cloud_Classification/codes_learning_notes/LSTM_model_pointcloud/board_3.txt', 'r')
for line in f:
    line=line.split(' ')
    row=[]
    for item in line:
        if '\n' in item:
            p=item.find('\n')
            item=item[0:p]
        row.append(float(item))
    train_data.append(row)
    train_labels.append([0,1,0,0,0,0,0,0,0,0,0,0])
f.close()

f = open('/Users/Fangyu/Documents/GitHub/Large_Scale_3D_Scene_Recognition_CVPR2017/Point_Cloud_Classification/codes_learning_notes/LSTM_model_pointcloud/bookcase_1.txt', 'r')
for line in f:
    line=line.split(' ')
    row=[]
    for item in line:
        if '\n' in item:
            p=item.find('\n')
            item=item[0:p]
        row.append(float(item))
    train_data.append(row)
    train_labels.append([0,0,1,0,0,0,0,0,0,0,0,0])
f.close()

f = open('/Users/Fangyu/Documents/GitHub/Large_Scale_3D_Scene_Recognition_CVPR2017/Point_Cloud_Classification/codes_learning_notes/LSTM_model_pointcloud/ceiling_1.txt', 'r')
for line in f:
    line=line.split(' ')
    row=[]
    for item in line:
        if '\n' in item:
            p=item.find('\n')
            item=item[0:p]
        row.append(float(item))
    train_data.append(row)
    train_labels.append([0,0,0,1,0,0,0,0,0,0,0,0])
f.close()

f = open('/Users/Fangyu/Documents/GitHub/Large_Scale_3D_Scene_Recognition_CVPR2017/Point_Cloud_Classification/codes_learning_notes/LSTM_model_pointcloud/chair_1.txt', 'r')
for line in f:
    line=line.split(' ')
    row=[]
    for item in line:
        if '\n' in item:
            p=item.find('\n')
            item=item[0:p]
        row.append(float(item))
    train_data.append(row)
    train_labels.append([0,0,0,0,1,0,0,0,0,0,0,0])
f.close()



with tf.Session() as sess:
    sess.run(init)
    step = 1
    count=0
    # Keep training until reach max iterations
    try:
        while step * batch_size < training_iters:
        #batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            batch_xs=np.array(train_data[count:count+batch_size])
            batch_ys=np.array(train_labels[count:count+batch_size])
            batch_xs = batch_xs.reshape((batch_size, n_steps, n_input_1))
        # Fit training using batch data
            sess.run(optimizer, feed_dict={x: batch_xs, y: batch_ys,
                                       istate_fw_1: np.zeros((batch_size, 2*n_hidden)),
                                       istate_bw_1: np.zeros((batch_size, 2*n_hidden))})
            if step % display_step == 0:
            # Calculate batch accuracy
                acc = sess.run(accuracy, feed_dict={x: batch_xs, y: batch_ys,
                                                istate_fw_1: np.zeros((batch_size, 2*n_hidden)),
                                                istate_bw_1: np.zeros((batch_size, 2*n_hidden))})
            # Calculate batch loss
                loss = sess.run(cost, feed_dict={x: batch_xs, y: batch_ys,
                                             istate_fw_1: np.zeros((batch_size, 2*n_hidden)),
                                             istate_bw_1: np.zeros((batch_size, 2*n_hidden))})
                print("Iter " + str(step*batch_size) + ", Minibatch Loss= " + "{:.6f}".format(loss) +
                  ", Training Accuracy= " + "{:.5f}".format(acc))
            step += 1
            count=count+batch_size
    except:
        pass
    print("Optimization Finished!")



    # Calculate accuracy for 128 mnist test images
    f = open('/Users/Fangyu/Documents/GitHub/Large_Scale_3D_Scene_Recognition_CVPR2017/Point_Cloud_Classification/codes_learning_notes/LSTM_model_pointcloud/board_2.txt', 'r')
    test_data=[]
    test_label=[]

    for line in f:
        line=line.split(' ')
        row=[]
        for item in line:
            if '\n' in item:
                p=item.find('\n')
                item=item[0:p]
            row.append(float(item))
        test_data.append(row)
        test_label.append([0,1,0,0,0,0,0,0,0,0,0,0])
    f.close()


    test_len = 128
    test_data = np.array(test_data[:test_len]).reshape((-1, n_steps, n_input_1))
    test_label =np.array(test_label[:test_len])
    print("Testing Accuracy:", sess.run(accuracy, feed_dict={x: test_data, y: test_label,
                                                             istate_fw_1: np.zeros((test_len, 2*n_hidden)),
                                                             istate_bw_1: np.zeros((test_len, 2*n_hidden))}))

    f = open('/Users/Fangyu/Documents/GitHub/Large_Scale_3D_Scene_Recognition_CVPR2017/Point_Cloud_Classification/codes_learning_notes/LSTM_model_pointcloud/chair_2.txt', 'r')
    test_data=[]
    test_label=[]

    for line in f:
        line=line.split(' ')
        row=[]
        for item in line:
            if '\n' in item:
                p=item.find('\n')
                item=item[0:p]
            row.append(float(item))
        test_data.append(row)
        test_label.append([0,0,0,0,1,0,0,0,0,0,0,0])
    f.close()


    test_len = 128
    test_data = np.array(test_data[:test_len]).reshape((-1, n_steps, n_input_1))
    test_label =np.array(test_label[:test_len])
    print("Testing Accuracy:", sess.run(accuracy, feed_dict={x: test_data, y: test_label,
                                                         istate_fw_1: np.zeros((test_len, 2*n_hidden)),
                                                         istate_bw_1: np.zeros((test_len, 2*n_hidden))}))

'''
for line in train_data:
    for x in line:
            if '\n' in str(x):
                print('true')

'''
