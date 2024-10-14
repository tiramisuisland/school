import tensorflow as tf

str_1 = tf.constant("Hello, Tensorflow")
str_2 = tf.convert_to_tensor("Hello, python")

# 印出字串内容與形狀
print("str_1:", str_1, ",shape:", str_1.shape)
print("str_2:", str_2, ",shape:", str_2.shape)