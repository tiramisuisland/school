import matplotlib.pyplot as plt
import tensorflow as tf
x = tf. linspace (-10., 10,100)
y = tf.nn. elu (x)
plt. plot(x, y)
plt. xlabel ("x")
plt. ylabel("ELU(x)")
plt. title("ELU Function")
plt. grid()
plt. show()