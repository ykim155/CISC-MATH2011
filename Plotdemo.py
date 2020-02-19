import matplotlib.pyplot as plt

x = [i / 20.0 for i in range(-20, 21)]  # values between -1 and 1
y1 = [xi * xi for xi in x]
y2 = [3 * xi + 1 for xi in x]

plt.plot(x, y1, 'k')  # a black curve
plt.plot(x, y2, 'b')  # a blue curve
plt.plot(x, y2, 'r+')  # red + markers

plt.xlim(-2, 1.5)
plt.ylim(-3, 6)

plt.show()

import random

x = [random.random() - 0.5 for i in range(1000)]
y = [random.random() - 0.5 for i in range(1000)]

plt.plot(x, y, 'y+')
plt.axhline(0, color='black')  # adds a horizontal axis
plt.axvline(0, color='black')  # adds a vertical axis
plt.show()


