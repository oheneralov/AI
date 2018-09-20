# Activation RELU + sigmoid for binary classification output + MSE loss function
# https://medium.com/@claude.coulombe/the-revenge-of-perceptron-learning-xor-with-tensorflow-eb52cbdf6c60
# https://aimatters.wordpress.com/2016/01/16/solving-xor-with-a-neural-network-in-tensorflow/
import tensorflow as tf
import time
import numpy as np

INPUT_XOR = [[0,0],[0,1],[1,0],[1,1]]
OUTPUT_XOR = [[0],[1],[1],[0]]

#  set up placeholders to hold the input data
# In XOR problem, there are four different training examples and each example has two features. 
# There are also four expected outputs, each with just one value (either a 0 or 1)
X = tf.placeholder(tf.float32, shape=[4,2], name = 'X')
Y = tf.placeholder(tf.float32, shape=[4,1], name = 'Y')

W = tf.Variable(tf.truncated_normal([2,2]), name = "W")
w = tf.Variable(tf.truncated_normal([2,1]), name = "w")

c = tf.Variable(tf.zeros([4,2]), name = "c")
b = tf.Variable(tf.zeros([4,1]), name = "b")

with tf.name_scope("hidden_layer") as scope:
    h = tf.nn.relu(tf.add(tf.matmul(X, W),c))

with tf.name_scope("output") as scope:
    y_estimated = tf.sigmoid(tf.add(tf.matmul(h,w),b))

with tf.name_scope("loss") as scope:
    loss = tf.reduce_mean(tf.squared_difference(y_estimated, Y)) 


with tf.name_scope("train") as scope:
    train_step = tf.train.GradientDescentOptimizer(0.01).minimize(loss)


init = tf.global_variables_initializer()
sess = tf.Session()


# TensorBoard tensorboard --logdir= /logs/xor.logs
# http://localhost:6006
writer = tf.summary.FileWriter("./logs/xor.logs", sess.graph)

sess.run(init)

t_start = time.clock()
for epoch in range(100001):
    sess.run(train_step, feed_dict={X: INPUT_XOR, Y: OUTPUT_XOR})
    if epoch % 10000 == 0:
        print("_"*80)
        print('Epoch: ', epoch)
        print('   y_estimated: ')
        for element in sess.run(y_estimated, feed_dict={X: INPUT_XOR, Y: OUTPUT_XOR}):
            print('    ',element)
        print('   W: ')
        for element in sess.run(W):
            print('    ',element)
        print('   c: ')
        for element in sess.run(c):
            print('    ',element)
        print('   w: ')
        for element in sess.run(w):
            print('    ',element)
        print('   b ')
        for element in sess.run(b):
            print('    ',element)
        print('   loss: ', sess.run(loss, feed_dict={X: INPUT_XOR, Y: OUTPUT_XOR}))
t_end = time.clock()
print("_"*80)
print('The elapsed time ', t_end - t_start)

#print('Testing')
#result = sess.run(loss, feed_dict={X: 1, Y: 1})
#print(result)

