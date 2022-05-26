import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np
x = np.arange(7,35)
print(x)
y = np.exp(x/3.0)
print(y)
f = interpolate.interp1d(x, y)
x1 = np.arange(8, 15)
print(x1)
y1 = f(x1)
print(y1)
plt.plot(x, y, 'o', x1, y1, '--')
plt.show()
