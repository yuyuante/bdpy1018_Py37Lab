import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 5, 0.1)
plt.figure(1)
plt.subplot(1, 3, 1)
plt.plot(t, t, 'r.-')
plt.subplot(1, 3, 2)
plt.plot(t, t ** 2, 'g*-')
plt.subplot(133)
plt.plot(t,t**3, 'b^--')
plt.show()
