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
    # print(Vol)


anim = FuncAnimation(fig, func=animate1, frames=range(100), interval=1)
plt.show()

# Number 2
norm = np.linalg.norm
print("norm = np.linalg.norm")
print("Making an orthogonal vector Q.")
Q = (1 / 3) * np.array([[2, -2, 1], [1, 2, 2], [2, 1, -2]])
print(Q)

print("Q-Skew from Def. 21")
Qskw = .5 * (Q - Q.T)
print(Qskw)

print("w is for omega, the axial vector. The axis in which the orthogonal vector rotates.")
w = np.array([Q[2, 1] - Q[1, 2], Q[0, 2] - Q[2, 0], Q[1, 0] - Q[0, 1]]).reshape((3, 1))
print(w)

print("We can see that Qskw @ w = 0. Then, 0.5(Q - Q.T)w = 0. After moving 1/2 and distributing w, we get Qw = Q.Tw.")
0 == Qskw @ w
print(
    "Multiply Q to both sides and you get Q^2w = QQ.Tw. Since Q is orthogonal, QQ.T is the identity matrix, I or I^2.")
print(Q @ Q.T)
print("Now we have: Q^2w = I^2w. If we move I^2w to the other side and factor out w, we get (Q^2-I^2)w.")
print("We can factor using the difference of squares to get: (Q+I)(Q-I)w = 0.")
# W not omega now.
print("Now either case can, leads to the conclusion that unit vector W exists, where QW = cW, c = +-1.")
W = w / norm(w)
print(Q @ W)
print(W)

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
f3 = np.array([shape[:, i] for i in i3]).T
f4 = np.array([shape[:, i] for i in i4]).T
fB = np.array([shape[:, i] for i in B]).T
fT = np.array([shape[:, i] for i in T]).T

faces = [f1, f2, f3, f4, fB, fT]

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

# Create Animation
fig = plt.figure()
ax = fig.gca(projection='3d')


def animate2(i):
    global Q, shape, faces

    shape = Q @ shape

    faces[0] = Q @ faces[0]
    faces[1] = Q @ faces[1]
    faces[2] = Q @ faces[2]
    faces[3] = Q @ faces[3]
    faces[4] = Q @ faces[4]
    faces[5] = Q @ faces[5]

    ax.clear()
    ax.plot(shape[0], shape[1], shape[2], '.k')

    ax.plot(faces[0][0], faces[0][1], faces[0][2], 'k')
    ax.plot(faces[1][0], faces[1][1], faces[1][2], 'k')
    ax.plot(faces[2][0], faces[2][1], faces[2][2], 'k')
    ax.plot(faces[3][0], faces[3][1], faces[3][2], 'k')
    ax.plot(faces[4][0], faces[4][1], faces[4][2], 'k')
    ax.plot(faces[5][0], faces[5][1], faces[5][2], 'k')

    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_zlim(-2.5, 2.5)


anim = FuncAnimation(fig, func=animate2, frames=range(100), interval=2)
plt.show()
