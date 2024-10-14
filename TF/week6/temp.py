import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# 加載 MNIST 數據集
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 將數據歸一化到 0-1 範圍
x_train, x_test = x_train / 255.0, x_test / 255.0

# 建立一個神經網路模型
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # 將 28x28 的圖像展平成一維數據
    layers.Dense(128, activation='relu'),  # 隱藏層，128 個神經元，ReLU 激活函數
    layers.Dropout(0.2),                   # Dropout 層，用來防止過擬合
    layers.Dense(10, activation='softmax') # 輸出層，10 個神經元對應 10 個分類，使用 softmax 激活函數
])

# 編譯模型
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 訓練模型
model.fit(x_train, y_train, epochs=5)

# 評估模型
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc}")

# 預測
predictions = model.predict(x_test)

# 顯示測試數據中的一個圖像及其預測結果
plt.figure()
plt.imshow(x_test[0], cmap=plt.cm.binary)
plt.title(f"Prediction: {predictions[0].argmax()}")
plt.show()
