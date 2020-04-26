import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Number 1
cos, sin, pi = math.cos, math.sin, math.pi

dt = 0.01  # time constant
fig, ax = plt.subplots()
l1, l2 = 4, 5

x = np.array([(0, 2, 2, 0, 0), (0, 0, 1, 1, 0)])  # rectangle vertices

S = np.array([(1, 0), (dt, 1)])  # shear matrix
L = np.diag([1 + dt * l1, 1 + dt * l2])  # diagonal matrix
R = np.array([(cos(2 * pi * dt), -sin(2 * pi * dt)), (sin(2 * pi * dt), cos(2 * pi * dt))])  # rotation matrix


def animate(i):
    global x, L

    x = L @ x
    x = S @ x
    x = R @ x

    ax.clear()

    # draw axes
    ax.set_xlim(-50, 100)
    ax.set_ylim(-50, 100)

    ax.plot(x[0], x[1])

    Vol = (x[0, 1] - x[0, 0]) * (x[1, 3] - x[1, 0])
    print(Vol)


animination = FuncAnimation(fig, func=animate, frames=range(100), interval=1)
plt.show()
