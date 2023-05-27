import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5,5,100)
y_1 = np.sin(x)
y_2 = np.cos(x)
y_3 = y_2*2

figure,(ax1,ax2,ax3) = plt.subplots(1,3,
  figsize=(6,2),
  dpi=600,
  # 共享y轴
  sharey=True)
figure.suptitle('以下三图共享了Y轴')
ax1.plot(x,y_1,c='blue',linestyle=':')
ax2.plot(x,y_2,c='orange',linestyle=':')
ax3.plot(x,y_3,c='r',linestyle=':')
plt.show()