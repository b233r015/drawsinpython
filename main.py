import matplotlib.pyplot as plt
import numpy as np

t = 100
mean = 0.0
std = 1.0


x = np.linspace(0, 2*np.pi, 100)

y = np.sin(x)

plt.plot(x,y)
plt.show()