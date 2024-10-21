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
print("Initial W:", W)

learn_rate = 0.11
n = 0
output_y = 0

def update():
    global X, Y, W, learn_rate, n
    n += 1
    output_y = np.sign(np.dot(X, W.T))
    W_change = learn_rate * (Y - output_y.T).dot(X) / int(X.shape[0])
    W = W_change + W

# 训练100次
for _ in range(100):
    update()
    print("Updated W:", W)
    print("Iteration:", n)
    output_y = np.sign(np.dot(X, W.T))
    if (output_y == Y.T).all():
        print("Converged")
        print("Iterations to converge:", n)
        break

k = -W[1] / W[2]
d = -W[0] / W[2]
print("k =", k)
print("d =", d)

xdata = np.linspace(0, 5)
plt.figure()
plt.plot(xdata, xdata * k + d, 'r', label='Decision Boundary')
plt.plot(X_pos[:, 0], X_pos[:, 1], 'bo', label='Positive Class')
plt.plot(X_neg[:, 0], X_neg[:, 1], 'yo', label='Negative Class')
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()
plt.show()
