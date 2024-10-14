import matplotlib.pyplot as plt
import numpy as np
x1 = np.linspace(0.0,2*np.pi)
y1 = np.sin(x1)

x2 = np.linspace(0.0,2*np.pi)
y2 = np.cos(x2)

plt.plot(x1, y1, 'r', label='sin')
plt.plot(x2, y2, 'b-o', label='cos')

plt.legend()
plt.show()