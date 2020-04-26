import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

cos, sin, pi = math.cos, math.sin, math.pi

# Number 1
dt = 0.01  # time constant
fig, ax = plt.subplots()
l1, l2 = 4, 5

x = np.array([(0, 2, 2, 0, 0), (0, 0, 1, 1, 0)])  # rectangle vertices

S = np.array([(1, 0), (dt, 1)])  # shear matrix
L = np.diag([1 + dt * l1, 1 + dt * l2])  # diagonal matrix
R = np.array([(cos(2 * pi * dt), -sin(2 * pi * dt)), (sin(2 * pi * dt), cos(2 * pi * dt))])  # rotation matrix


def animate1(i):
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


anim = FuncAnimation(fig, func=animate1, frames=range(100), interval=1)
plt.show()

# Number 3

# Create a 3D Object. This is a cube
shape = np.array([[0, 0, 1, 1, 0, 0, 1, 1],
                  [0, 1, 0, 1, 0, 1, 0, 1],
                  [0, 0, 0, 0, 1, 1, 1, 1]])

# Vertices and Faces
i1 = [0, 2, 6, 4, 0]
i2 = [2, 3, 7, 6, 2]
i3 = [1, 3, 7, 5, 1]
i4 = [0, 1, 5, 4, 0]
B = [0, 1, 3, 2, 0]
T = [4, 5, 7, 6, 4]

f1 = np.array([shape[:, i] for i in i1]).T
f2 = np.array([shape[:, i] for i in i2]).T


f1 = [tuple(shape[:, i]) for i in i1]
f2 = [tuple(shape[:, i]) for i in i2]
f3 = [tuple(shape[:, i]) for i in i3]
f4 = [tuple(shape[:, i]) for i in i4]
fB = [tuple(shape[:, i]) for i in B]
fT = [tuple(shape[:, i]) for i in T]

faces = [f1, f2, f3, f4, fB, fT]
colors = ['r', 'b', 'g', 'k', 'm', 'c']

# Create the rotation matrix to rotate about the axis
norm = np.linalg.norm
u = np.array([1, 0, 1])
v = np.array([1, 0, -1])
w = np.cross(u, v)

u = u.reshape((3, 1)) / norm(u)
v = v.reshape((3, 1)) / norm(v)
w = w.reshape((3, 1)) / norm(w)

Q = np.hstack([u, v, w])
th = pi / 100.0
R = cos(th) * u @ u.T - sin(th) * u @ v.T + sin(th) * v @ u.T + cos(th) * v @ v.T
Q = w @ w.T + R

fig = plt.figure()
ax = fig.gca(projection='3d')

for (f, c) in zip(faces, colors):
    poly = Poly3DCollection([f])
    poly.set_color(c)
    ax.add_collection3d(poly)
    vx = [t[0] for t in f]
    vy = [t[1] for t in f]
    vz = [t[2] for t in f]
    V = np.array([vx, vy, vz])
    ax.plot(V[0], V[1], V[2], 'k', linewidth=3)

# Create Animation
fig = plt.figure()
ax = fig.gca(projection='3d')


def animate2(i):
    global Q, shape, faces

    shape = Q @ shape

    ax.clear()
    ax.plot(shape[0], shape[1], shape[2], '.k')
    ax.plot(V[0], V[1], V[2], 'k')

    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_zlim(-2.5, 2.5)


anim = FuncAnimation(fig, func=animate2, frames=range(100), interval=2)
plt.show()
