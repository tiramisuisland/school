import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
import matplotlib.pyplot as plt

# 資料前處理函數
def preprocess(x, y):
    x = tf.cast(x, dtype=tf.float32) / 255.0
    x = tf.reshape(x, [28, 28, 1])
    y = tf.cast(y, dtype=tf.int32)
    return x, y

# 批次大小
batchs = 32

# 載入 mnist 資料集 (60000 筆訓練資料，10000 筆測試資料，影像大小為 28x28)
(train_Data, train_Label), (test_Data, test_Label) = mnist.load_data()

# 建立訓練資料集
db = tf.data.Dataset.from_tensor_slices((train_Data, train_Label))
db = db.map(preprocess).shuffle(10000).batch(batchs)

# 建立測試資料集
db_test = tf.data.Dataset.from_tensor_slices((test_Data, test_Label))
db_test = db_test.map(preprocess).batch(batchs)

# 建立 LeNet 模型
LeNet5Model = Sequential([
    # 第一個卷積層：6 個 5x5 的卷積核，激活函數為 relu
    Conv2D(6, kernel_size=5, strides=1, padding='same', activation='relu'),
    # 最大池化層：2x2，步長為 2
    MaxPooling2D(pool_size=2, strides=2),
    # 第二個卷積層：16 個 5x5 的卷積核，激活函數為 relu
    Conv2D(16, kernel_size=5, strides=1, padding='same', activation='relu'),
    # 最大池化層：2x2，步長為 2
    MaxPooling2D(pool_size=2, strides=2),
    # 平坦化，方便進入全連接層
    Flatten(),
    # 第一個全連接層
    Dense(120, activation='relu'),
    # 第二個全連接層
    Dense(84, activation='relu'),
    # 輸出層 (分類 10 類數字，使用 softmax 激活函數)
    Dense(10, activation='softmax')
])

# 檢視模型架構
LeNet5Model.build(input_shape=(None, 28, 28, 1))
print(LeNet5Model.summary())

# 設定優化器
optimizer = tf.keras.optimizers.SGD(learning_rate=0.01)

# 編譯模型，定義損失函數與評估指標
LeNet5Model.compile(
    optimizer=optimizer,
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 訓練模型
hist = LeNet5Model.fit(db, epochs=5, validation_data=db_test)

# 繪製訓練與驗證的準確率與損失圖
val_acc = hist.history['val_accuracy']
acc = hist.history['accuracy']
val_loss = hist.history['val_loss']
loss = hist.history['loss']

plt.plot(np.arange(len(val_loss)), val_loss, label='val_loss')
plt.plot(np.arange(len(loss)), loss, label='loss')
plt.ylim(0, 1.0)
plt.xlabel('EPOCHS')
plt.ylabel('LOSS')
plt.legend()
plt.grid()
plt.show()

plt.plot(np.arange(len(val_acc)), val_acc, label='val_acc')
plt.plot(np.arange(len(acc)), acc, label='acc')
plt.ylim(0, 1.0)
plt.xlabel('EPOCHS')
plt.ylabel('ACC')
plt.legend()
plt.grid()
plt.show()
