import numpy as np
import math
import matplotlib as plt
from matplotlib.animation import FuncAnimation

# Number 1
dt = 0.1  # time constant
fig, ax = plt.subplot()
l1, l2 = 4, 5

x = np.array([(0, 0, 2, 2, 0), (0, 1, 1, 0, 0)])  # rectangle vertices
L = np.diag([1 + dt * l1, 1 + dt * l2])  # diagonal matrix


def animate(i):
    global x, L
    x = L @ x

    ax.clear()

    # draw axes
    ax.set_xlim(-8, 10)
    ax.set_ylim(-8, 10)

    ax.plot(x[0], x[1])

    Vol = (x[0, 1] - x[0, 0]) * (x[1, 3] - x[1, 0])
    print(Vol)


animination = FuncAnimation(fig, func=animate, frames=range(100), interval=2)
plt.show
