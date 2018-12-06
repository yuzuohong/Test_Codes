import tensorflow as tf

node1 = tf.constant(3.0,name='node1')
node2 = tf.constant(8.0,name='node2')
node3 = tf.add(node1,node2,name='node3')

node4 = tf.multiply(node1,node2,name='node4')
node5 = tf.multiply(node3,node4,name='node5')

node6 = node5 * 10

print(node1,node2,node3,node4,node5,node6)

sess = tf.Session()
print(sess.run([node1, node2, node3, node4, node5, node6]))

output = sess.run(node6)

writer = tf.summary.FileWriter('./my_graph',sess.graph)

writer.close()

sess.close()


