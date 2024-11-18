import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# 遊戲選項
choices = ["Scissors", "Rock", "Paper"]  # 0: 剪刀, 1: 石頭, 2: 布

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

# 初始化數據集
data = []
labels = []

# 即時訓練函數
def train_model():
    if len(data) < 5:  # 確保至少有一定數據量
        print("Not enough data to train. Need at least 5 records.")
        return

    # 準備數據
    inputs = torch.tensor(data, dtype=torch.float32)
    targets = torch.tensor(labels, dtype=torch.long)

    # 訓練模型
    for epoch in range(50):  # 每次訓練 50 個 epoch
        outputs = model(inputs)
        loss = criterion(outputs, targets)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print("Model updated with real-time data!")

# 預測玩家下一步的選擇
def get_robot_choice(player_history):
    if len(player_history) < 2:
        return np.random.randint(0, 3)  # 如果數據不足，隨機選擇

    # 使用最近兩次選擇作為輸入
    input_data = torch.tensor(player_history[-2:], dtype=torch.float32).unsqueeze(0)
    prediction = model(input_data)
    predicted_player_choice = torch.argmax(prediction, dim=1).item()

    # 機器人選擇能贏的手勢
    robot_choice = (predicted_player_choice + 1) % 3  # 剪刀 -> 石頭, 石頭 -> 布, 布 -> 剪刀
    return robot_choice

# 判斷輸贏
def determine_winner(player, robot):
    """
    判斷輸贏：0 平局, 1 玩家贏, -1 機器人贏
    """
    if player == robot:
        return 0
    elif (player == 0 and robot == 2) or (player == 1 and robot == 0) or (player == 2 and robot == 1):
        return 1
    else:
        return -1

# 與玩家互動
print("Welcome to Rock-Paper-Scissors!")
print("Enter your choice: 0 for Scissors, 1 for Rock, 2 for Paper")

player_history = []

while True:
    # 玩家輸入
    try:
        player_choice = int(input("Your choice: "))
        if player_choice not in [0, 1, 2]:
            print("Invalid choice. Please choose 0, 1, or 2.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # 機器人選擇
    if len(player_history) < 2:
        print("Collecting data... Play two rounds first!")
        robot_choice = np.random.randint(0, 3)
    else:
        robot_choice = get_robot_choice(player_history)

    player_history.append(player_choice)

    # 保存數據
    if len(player_history) >= 2:
        data.append(player_history[-2:])  # 最近兩次選擇作為輸入
        labels.append(player_choice)     # 下一步選擇作為標籤

    # 顯示選擇
    print(f"You chose: {choices[player_choice]}")
    print(f"Robot chose: {choices[robot_choice]}")

    # 判斷結果
    result = determine_winner(player_choice, robot_choice)
    if result == 0:
        print("It's a draw!")
    elif result == 1:
        print("You win!")
    else:
        print("Robot wins!")

    # 實時訓練模型
    train_model()

    # 是否繼續
    cont = input("Play again? (y/n): ").lower()
    if cont != 'y':
        break

print("Thanks for playing!")
