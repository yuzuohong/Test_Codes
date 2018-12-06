import tensorflow as tf


a = int(input('enter a number for variable a:'))

node1 = tf.Variable(a)

b = int(input('enter a number for variable b:'))

node2 = tf.Variable(b)

node3 = tf.add(node1,node2)

node4 = tf.multiply(node3,node3)

node5 = tf.divide(node4,(node3+node2+node1))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    writer = tf.summary.FileWriter('D:\Python\Test_Codes',sess.graph)
    print(sess.run(node5))

writer.close()

