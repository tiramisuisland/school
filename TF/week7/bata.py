import numpy as np
import matplotlib.pyplot as plt

# 指定正类和负类的数据
X_pos = np.array([[1, 3], [2, 4], [3, 3], [2, 3], [4, 5], [3, 2], [2, 2]])  # 正类样本
X_neg = np.array([[3, 1], [1, 2], [2, 1]])  # 负类样本

# 添加偏置项1
X = np.concatenate([np.hstack([np.ones((7, 1)), X_pos]), np.hstack([np.ones((3, 1)), X_neg])])
Y = np.concatenate([np.ones(7), -np.ones(3)])  # 正类标签为1，负类标签为-1

# 随机初始化权重
W = (np.random.random(3) - 0.5) * 2
print("初始权重 W:", W)

learn_rate = 0.11
n = 0
output_y = 0

# 定义权重更新函数
def update():
    global X, Y, W, learn_rate, n
    n += 1
    output_y = np.sign(np.dot(X, W.T))  # 计算输出
    W_change = learn_rate * (Y - output_y.T).dot(X) / int(X.shape[0])  # 计算权重变化
    W = W_change + W  # 更新权重

# 训练100次或收敛
for _ in range(100):
    update()
    print("更新后的权重 W:", W)
    print("第", n, "次迭代")
    output_y = np.sign(np.dot(X, W.T))
    if (output_y == Y.T).all():
        print("已收敛")
        print("收敛次数:", n)
        break

# 计算决策边界的斜率和截距
k = -W[1] / W[2]
d = -W[0] / W[2]
print("k =", k)
print("d =", d)

# 绘制决策边界
xdata = np.linspace(0, 5)
plt.figure()
plt.plot(xdata, xdata * k + d, 'r', label='决策边界')
plt.plot(X_pos[:, 0], X_pos[:, 1], 'bo', label='正类')
plt.plot(X_neg[:, 0], X_neg[:, 1], 'yo', label='负类')
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()
plt.show()
