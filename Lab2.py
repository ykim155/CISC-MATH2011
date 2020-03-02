import cmath
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# for easy use
pi = math.pi
sin = math.sin
cos = math.cos
acos = math.acos
exp = cmath.exp


def Real(z):  # list of real values
    a = [zi.real for zi in z]
    return a


def Imag(z):  # list of imaginary values
    b = [zi.imag for zi in z]
    return b


def cdist(z1, z2):  # dist between two complex numbers
    return math.sqrt(((z1.real - z2.real) ** 2 + ((z1.imag - z2.imag) ** 2)))


def pivot_simp(z, a):  # simple pivot
    return [z0 * exp(a * 1j) for z0 in z]


def pivot(z, z0, a):  # pivot in relation to a specific point
    return [z0 + (zi - z0) * exp(a * 1j) for zi in z]


def straighten(z):  # straighten the shape
    z_dist = cdist(z[0], z[1])
    z1_x = z[0].real
    straight_angle = acos(z1_x / z_dist)
    return pivot_simp(z, - (straight_angle + alpha))


def avg(l):  # find the average of a list
    return sum(l)/len(l)


N = 3  # number of sides
theta = 2 * N * pi  # total angle of rotation
alpha = pi / N  # half of the vertex angle

s = 300  # number of time steps, from 0 to 1
time = [i / s for i in range(s + 1)]  # times 0 to 1

z = [3 * exp(2 * alpha * 1j * k) - 3 for k in range(N)]  # shape
z = z + [z[0]]  # make shape cyclic
z = straighten(z)  # straighten the shape so bottom is parallel to x-axis

tracer = []  # tracer list to be appended to

h = cdist(z[1], z[2])  # hypotenuse of the line between z1 and z2
a = z[2].real - z[1].real  # the projection of the hypotenuse
angle_of_rotation = acos(a / h)  # angle between the two

mu = [-angle_of_rotation * ti for ti in time]  # intermediate angles between one rotation

# set up plot shape
fig, ax = plt.subplots()
ax.axis('square')


def animate(i):  # animation function
    global z, N
    i_pivot = 1 + i // s % N

    dth = mu[i_pivot + 1] - mu[i_pivot]  # diff in angles
    z = pivot(z, z[i_pivot], dth)  # actual pivot every frame

    x = Real(z)  # list of real z values
    y = Imag(z)  # list of imag z values

    # get rid of duplicates for the center
    xc = set(x)
    yc = set(y)

    # append z[0], the tracer vertex
    tracer.append(z[0])

    tx = Real(tracer)  # list of real tracer values
    ty = Imag(tracer)  # list of imag tracer values

    cx = avg(list(xc))  # find x coord of centroid
    cy = avg(list(yc))  # find y coord of centroid

    # plotting
    ax.clear()
    ax.set_xlim(-3, x[i_pivot] + 7)  # plot new x-lim every pivot vertex change
    ax.set_ylim(0, 10)  # y-lim
    ax.plot(x, y, 'k')  # plot the shape
    plt.plot(cx, cy, 'ko')  # plot the center
    plt.plot(tx, ty, 'g')  # plot the tracer curve
    ax.plot(x[0], y[0], 'go')  # plot the tracer dot


animation = FuncAnimation(fig, func=animate, frames=range(N * len(time) + 1), interval=1)  # activate animation

plt.show()
