import tensorflow as tf
a1 = tf.constant([[3.0, 3.0, 3.0],
                  [3.0, 3.0, 3.0],
                  [3.0, 3.0, 3.0]])

a2 = tf.constant([[1.5, 1.5, 1.5],
                  [1.5, 1.5, 1.5],
                  [1.5, 1.5, 1.5]])

add1 = tf.add(a1, a2)
add2 = a1 + a2
print(add1, add2, sep='\n')

#a1 - a2
print(tf.subtract(a1, a2))
#a1 * a2
print(tf.multiply(a1, a2))
#a1 / a2
print(tf.divide(a1, a2))