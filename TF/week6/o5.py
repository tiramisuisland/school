import matplotlib.pyplot as plt
import tensorflow as tf
x = tf. linspace (-10., 10,100)
y = tf.nn. relu (x)
plt. plot(x, y)
plt. xlabel ("x")
plt. ylabel("Relu(x)")
plt. title("Relu Function")
plt. grid()
plt. show()