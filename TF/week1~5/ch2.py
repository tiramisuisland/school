import matplotlib.pyplot as plt
x1 = [1,2,3]

y1 = [2,1,2]

x2 = [1,2,3]
y2 = [1,3,1]

plt.plot(x1, y1, label='First')
plt.plot(x2, y2, label='Second')
plt.xlabel('x')

plt.ylabel('y')

plt.title('curve function')
plt.legend()
plt.show()