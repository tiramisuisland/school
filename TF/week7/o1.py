import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

X = np.array([[1,3,3], [1,4,3],[1,1,1]])

Y  = np.array([1,1,-1])   

W = (np.random.random(3)-0.5)*2
print (W)

learn_rate = 0.11
n=0
output_y = 0

def update():
    global X,Y,W,learn_rate,n
    n+=1
    output_y = np.sign(np.dot(X,W.T))
    W_change = learn_rate*(Y-output_y.T).dot(X)/int(X.shape[0])
    W = W_change + W

for _ in range(100):
    update()
    print (W)
    print (n)
    output_y = np.sign(np.dot(X,Y.T))
    if (output_y == Y.T).all():
        print("完成")
        print("ecoch:收斂次數",n)
        break

x1 = [3,4]
y1 = [3,3]

x2 = [1]
y2 = [1]

k = -W[1]/W[2]
d= -W[0]/W[2]
print("k=",k)
print("d=",d)

xdata = np.linspace(0,5)
plt.figure()
plt.plot(xdata,xdata*k+d,'r')
plt.plot(x1,y1,'bo')
plt.plot(x2,y2,'yo')
plt.show()