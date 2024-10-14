import tensorflow as tf
import numpy as np

miltiMaterixValue = tf.constant([[[1.2, 2.4], [3.6, 4.8]], [[2.1, 4.2], [6.2, 8.4]]])

print(miltiMaterixValue)
print(miltiMaterixValue.numpy())

tfconv = tf.convert_to_tensor([[[1.2, 2.4], [3.6, 4.8]], [[2.1, 4.2], [6.2, 8.4]]])

print(tfconv)

tfconv = tf.convert_to_tensor(np.array([[[1.2, 2.4], [3.6, 4.8]], [[2.1, 4.2], [6.2, 8.4]]]))

print(tfconv)