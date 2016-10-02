import tensorflow as tf
#from tensorflow.python.ops.constant_op import constant
import numpy as np
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


# Parameters
learning_rate = 0.001
training_iters = 1000
batch_size = 128

n_input=6


n_steps = 1 # timesteps
n_hidden = 128 # hidden layer num of features
#n_classes = 10 # MNIST total classes (0-9 digits)
n_classes=12#pointcloud total classes(5 furnitures,7 structral parts)

x = tf.placeholder("float", [batch_size, n_steps, n_input])
y = tf.placeholder("float", [batch_size, n_classes])

istate = tf.placeholder("float", [batch_size, 2*n_hidden])


softmax_w = tf.placeholder("float", [batch_size, 2*n_hidden])
softmax_b = tf.placeholder("float", [batch_size, 2*n_hidden])

number_of_layers=8

lstm = tf.nn.rnn_cell.BasicLSTMCell(n_hidden, forget_bias=1.0,state_is_tuple=True)
stacked_lstm = tf.nn.rnn_cell.MultiRNNCell([lstm] * number_of_layers,state_is_tuple=True)
#initial_state = state = stacked_lstm.zero_state(batch_size, tf.float32)
initial_state = state = np.zeros((batch_size, 2*n_hidden))


def Network(_x,_state):
    output, state = stacked_lstm(_x,_state)
    print (output,state)
    result = tf.matmul(output, softmax_w) + softmax_b
    return result

pred=Network(x,istate)
'''state是如何定义的?'''
loss=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(pred,y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)

correct_pred = tf.equal(tf.argmax(pred,1), tf.argmax(y,1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

step=0
count=0
while step * batch_size < training_iters:
#    try:
        batch_xs=np.array(train_data[count:count+batch_size])
        batch_ys=np.array(train_labels[count:count+batch_size])

        batch_xs = batch_xs.reshape((batch_size, 1, 6))
        # 每次处理一批词语后更新状态值.
        # LSTM 输出可用于产生下一个词语的预测

        sess.run(optimizer, feed_dict={x: batch_xs, y: batch_ys,
                                        istate:initial_state})
        print(loss)

        step += 1
        count=count+batch_size
#    except:
#        pass


print("Optimization Finished!")
