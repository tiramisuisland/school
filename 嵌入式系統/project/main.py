import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# 遊戲選項
choices = ["Scissors", "Rock", "Paper"]  # 0: 剪刀, 1: 石頭, 2: 布

# 數據集 (玩家模式和機器人應對)
# 假設玩家過去的選擇模式是循環的
data = torch.tensor([
    [0, 1],  # 剪刀 -> 石頭
    [1, 2],  # 石頭 -> 布
    [2, 0],  # 布 -> 剪刀
    [1, 0],  # 石頭 -> 剪刀
    [2, 1],  # 布 -> 石頭
    [0, 2]   # 剪刀 -> 布
], dtype=torch.float32)

# 標籤 (玩家的下一步選擇)
labels = torch.tensor([1, 2, 0, 0, 1, 2], dtype=torch.long)

# 定義神經網絡
class RPSModel(nn.Module):
    def __init__(self):
        super(RPSModel, self).__init__()
        self.fc1 = nn.Linear(2, 10)  # 第一層
        self.fc2 = nn.Linear(10, 10)  # 第二層
        self.fc3 = nn.Linear(10, 3)  # 輸出層 (三個選項)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# 初始化模型
model = RPSModel()

# 定義損失函數和優化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# 訓練模型
epochs = 100
for epoch in range(epochs):
    # 前向傳播
    outputs = model(data)
    loss = criterion(outputs, labels)

    # 反向傳播和優化
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 10 == 0:
        print(f"Epoch [{epoch + 1}/{epochs}], Loss: {loss.item():.4f}")

print("Model training complete!")
