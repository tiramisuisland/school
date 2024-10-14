import matplotlib.pyplot as plt
import tensorflow as tf
x = tf. linspace (-10., 10,100)
y = tf.nn. sigmoid (x)
plt. plot(x, y)
plt. xlabel ("x")
plt. ylabel("Sigmoid(x)")
plt. title("Sigmoid Function")
plt. grid()
plt. show()