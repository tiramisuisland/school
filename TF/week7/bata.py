import numpy as np
import matplotlib.pyplot as plt

# 将正类和负类样本写在一起
X = np.vstack([[1, 3], [2, 4], [3, 3], [2, 3], [4, 5], [3, 2], [2, 2], 
               [3, 1], [1, 2], [2, 1]])  # 合并后的样本

# 添加偏置项1
X = np.hstack([np.ones((X.shape[0], 1)), X])
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
plt.plot(X[:7, 1], X[:7, 2], 'bo', label='Positive Class')  # 正类样本
plt.plot(X[7:, 1], X[7:, 2], 'yo', label='Negative Class')  # 负类样本
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()
plt.show()
