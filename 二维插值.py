import numpy as np
from scipy.interpolate import interp2d
import matplotlib.pyplot as plt
x = np.linspace(0, 4, 13)
y = np.array([0, 2, 3, 3.5, 3.75, 3.875, 3.9375, 4])
X, Y = np.meshgrid(x, y)
Z = np.sin(np.pi*X/6) * np.exp(Y/3)
x2 = np.linspace(0, 4, 65)
y2 = np.linspace(0, 4, 65)
f1 = interp2d(x, y, Z, kind='cubic')
Z2 = f1(x2, y2)
f2 = interp2d(x,y,Z,kind='linear')
Z3 = f2(x2,y2)
fig, ax = plt.subplots(nrows=1, ncols=3)
ax[0].pcolormesh(X, Y, Z,cmap='rainbow')
X2, Y2 = np.meshgrid(x2, y2)
ax[1].pcolormesh(X2, Y2, Z2,cmap='rainbow')
X3, Y3 = np.meshgrid(x2, y2)
ax[2].pcolormesh(X3, Y3, Z3,cmap='rainbow')
ax[0].set_title('origin')
ax[1].set_title('cubic')
ax[2].set_title('linear')
plt.show()