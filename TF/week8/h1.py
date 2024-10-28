import matplotlib.pyplot as plt
import numpy as np
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# 定義 data 與 label
x = np.array([[0., 0.], [1., 0.], [0., 1.], [1., 1.]])
y = np.array([[0.], [1.], [1.], [0.]])

X = tf.placeholder(shape=(None, 2), dtype=tf.float32)
Y = tf.placeholder(shape=(None, 1), dtype=tf.float32)

# 定義層數與神經元數量
w1 = tf.Variable(tf.random.normal(shape=(2, 4)))
b1 = tf.Variable(tf.random.normal(shape=(1, 4)))
w2 = tf.Variable(tf.random.normal(shape=(4, 1)))
b2 = tf.Variable(tf.random.normal(shape=(1, 1)))

# 前向傳播
hidden_layer = tf.sigmoid(tf.matmul(X, w1) + b1)
output_layer = tf.sigmoid(tf.matmul(hidden_layer, w2) + b2)

# 損失函數
loss = tf.reduce_sum(tf.square(Y - output_layer))

# 定義優化器
train = tf.train.AdamOptimizer(learning_rate=0.05).minimize(loss)

# 初始化
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
losses = []

# 訓練
epochs = 800
for epoch in range(epochs + 1):
    sess.run(train, feed_dict={X: x, Y: y})
    if epoch % 80 == 0:
        losses.append(sess.run(loss, feed_dict={X: x, Y: y}))

# 輸出預測值
print(sess.run(output_layer, feed_dict={X: x}))

# 繪製 loss 曲線
plt.figure(figsize=(8, 4))
plt.plot(np.linspace(0, 800, 11), losses)
plt.xticks(np.linspace(0, 800, 11))
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.show()

sess.close()
