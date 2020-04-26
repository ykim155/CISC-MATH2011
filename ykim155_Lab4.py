import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

cos, sin, pi = math.cos, math.sin, math.pi

# Number 1
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

# Number 3

# Create a 3D Object
x = np.array([(0, 1, 1, 0, 0.5)
              (0, 0, 1, 1, 0.5)
              (0, 0, 0, 0, 0.5)])
fig =  plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x[0], x[1], x[2], '.b')
plt.show()

# Create the rotation matrix to rotate about the axis
norm = np.linalg.norm
u = np.array([1, 0, 1])
v = np.array([1, 0, 1])
w = np.cross(u, w)

u = u.reshape((3, 1)) / norm(u)
v = v.reshape((3, 1)) / norm(v)
w = w.reshape((3, 1)) / norm(w)

Q = np.hstack([u, v, w])
th = pi / 20.0
R = cos(th) * u @ u.T - sin(th) * u @ v.T + sin(th) * v @ u.T + cos(th) * v @ v.T
Q = w @ w.T + R

# Create Animation

def animate(i):
