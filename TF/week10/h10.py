from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# 加載數據集
dataset = np.loadtxt("TF\week10\pima-indians-diabetes.csv", delimiter=",")
data = dataset[:, 0:8]  # 特徵值
label = dataset[:, 8]   # 標籤值

# 輸出資料的形狀
print("data.shape:", data.shape)  # 輸出資料集的維度
print("label.shape:", label.shape)  # 輸出標籤集的維度

# 1. 定義模型
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))  # 第一層，12個神經元
model.add(Dense(8, activation='relu'))               # 第二層，8個神經元
model.add(Dense(1, activation='sigmoid'))            # 輸出層，1個神經元

# 輸出模型架構
print(model.summary())

# 2. 編譯模型
model.compile(
    loss='binary_crossentropy', 
    optimizer='adam', 
    metrics=['accuracy']
)

# 3. 訓練模型
history = model.fit(
    data, label, 
    epochs=100,          # 訓練100個epoch
    batch_size=10,       # 每批次處理10筆資料
    validation_split=0.2, # 20%的數據用作驗證集
    verbose=2            # 輸出詳細的訓練過程
)

# 輸出訓練歷史
print("history:", history.history)

# 4. 模型評估
loss, accuracy = model.evaluate(data, label)
print("Loss: %.2f, Accuracy: %.2f%%" % (loss, accuracy * 100))

# 5. 預測測試
probabilities = model.predict(data)
predictions = [int(np.round(x)) for x in probabilities]

# 計算預測準確率
accuracy = np.mean(predictions == label)
print("Prediction Accuracy: %.2f%%" % (accuracy * 100))
